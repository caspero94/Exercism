export class TranslationService {
  constructor(api) {
    this.api = api;
  }

  free(text) {
    return this.api.fetch(text).then((result) => result.translation);
  }

  batch(texts) {
    if (texts.length === 0) return Promise.reject(new BatchIsEmpty());
    const promesas = texts.map((text) => this.free(text));
    return Promise.all(promesas);
  }

  /**
   * Requests the service for some text to be translated.
   *
   * Note: the request service is flaky, and it may take up to three times for
   *       it to accept the request.
   *
   * @param {string} text
   * @returns {Promise<void>}
   */

  request(text) {
    const prom = () =>
      new Promise((resolve, reject) => {
        this.api.request(text, (result) => {
          result ? reject(result) : resolve();
        });
      });
    return prom().catch(prom).catch(prom);
  }

  /**
   * Retrieves the translation for the given text
   *
   * - Rejects with an error if the quality can not be met
   * - Requests a translation if the translation is not available, then retries
   *
   * @param {string} text
   * @param {number} minimumQuality
   * @returns {Promise<string>}
   */
  premium(text, minimumQuality) {
    return this.api
      .fetch(text)
      .catch(() => {
        return this.request(text).then(() => this.api.fetch(text));
      })
      .then((result) => {
        if (result.quality < minimumQuality) {
          throw new QualityThresholdNotMet();
        }
        return result.translation;
      });
  }
}

/**
 * This error is used to indicate a translation was found, but its quality does
 * not meet a certain threshold. Do not change the name of this error.
 */
export class QualityThresholdNotMet extends Error {
  /**
   * @param {string} text
   */
  constructor(text) {
    super(
      `
The translation of ${text} does not meet the requested quality threshold.
    `.trim()
    );

    this.text = text;
  }
}

/**
 * This error is used to indicate the batch service was called without any
 * texts to translate (it was empty). Do not change the name of this error.
 */
export class BatchIsEmpty extends Error {
  constructor() {
    super(
      `
Requested a batch translation, but there are no texts in the batch.
    `.trim()
    );
  }
}
