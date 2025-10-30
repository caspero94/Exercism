//
// This is only a SKELETON file for the 'Promises' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const promisify = (callback) => {
  return (...args) => {
    return new Promise((resolve, reject) => {
      callback(...args, (error, result) => {
        if (error) reject(error);
        else resolve(result);
      });
    });
  };
};

export const all = (promises) => {
  return new Promise((resolve, reject) => {
    const results = [];
    let completed = 0;
    if (!promises) resolve();
    if (promises.length === 0) resolve(results);

    promises.forEach((p, index) => {
      Promise.resolve(p)
        .then((value) => {
          results[index] = value;
          completed += 1;
          if (completed === promises.length) resolve(results);
        })
        .catch(reject);
    });
  });
};

export const allSettled = (promises) => {
  return new Promise((resolve) => {
    if (!promises) resolve();
    if (promises.length === 0) resolve([]);

    const results = [];
    let completed = 0;

    promises.forEach((p, index) => {
      Promise.resolve(p)
        .then((value) => {
          results[index] = value;
        })
        .catch((error) => {
          results[index] = error;
        })
        .finally(() => {
          completed += 1;
          if (completed === promises.length) resolve(results);
        });
    });
  });
};

export const race = (promises) => {
  return new Promise((resolve, reject) => {
    if (!promises) resolve();
    if (promises.length === 0) resolve([]);

    promises.forEach((p) => {
      Promise.resolve(p)
        .then((value) => {
          resolve(value);
        })
        .catch((error) => {
          reject(error);
        });
    });
  });
};

export const any = (promises) => {
  return new Promise((resolve, reject) => {
    if (!promises) resolve();
    if (promises.length === 0) resolve([]);
    let rejections = 0;
    const errors = [];
    promises.forEach((p, index) => {
      Promise.resolve(p)
        .then((value) => {
          resolve(value);
        })
        .catch((error) => {
          errors[index] = error;
          rejections += 1;
          if (rejections === promises.length) reject(errors);
        });
    });
  });
};
