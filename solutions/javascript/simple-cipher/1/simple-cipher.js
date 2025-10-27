export class Cipher {
  constructor(key) {
    this._key = key ?? Cipher.#generateRandomKey();
  }

  static #generateRandomKey(length = 100) {
    return Array.from({ length }, () =>
      String.fromCharCode(97 + Math.floor(Math.random() * 26))
    ).join("");
  }

  encode(plainText) {
    let chiperText = "";
    for (let i = 0; i < plainText.length; i++) {
      let shift = this._key[i % this._key.length].charCodeAt(0) - 97;
      let plainCode = plainText[i].charCodeAt(0) - 97;
      let encode = (plainCode + shift) % 26;
      chiperText += String.fromCharCode(encode + 97);
    }
    return chiperText;
  }

  decode(chiperText) {
    let plainText = "";
    for (let i = 0; i < chiperText.length; i++) {
      let shift = this._key[i % this._key.length].charCodeAt(0) - 97;
      let chiperCode = chiperText[i].charCodeAt(0) - 97;
      let decode = (chiperCode - shift + 26) % 26;
      plainText += String.fromCharCode(decode + 97);
    }
    return plainText;
  }
  set key(key) {
    this._key = key;
  }

  get key() {
    return this._key;
  }
}
