//
// This is only a SKELETON file for the 'Rotational Cipher' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
// A-Z = 65-90
// a-z = 97-122

export const rotate = (plain, shift) => {
  let cipher = "";
  const ALPHABET_SIZE = 26;
  const LOWER_CASE_BASE = "a".charCodeAt(0);
  const UPPER_CASE_BASE = "A".charCodeAt(0);

  shift = shift % ALPHABET_SIZE;

  for (let i = 0; i < plain.length; i++) {
    const char = plain[i];
    const charCode = char.charCodeAt(0);

    let base;

    if (charCode >= LOWER_CASE_BASE && charCode <= 122) base = LOWER_CASE_BASE;
    else if (charCode >= UPPER_CASE_BASE && charCode <= 90)
      base = UPPER_CASE_BASE;
    else {
      cipher += char;
      continue;
    }
    cipher += String.fromCharCode(
      ((charCode - base + shift) % ALPHABET_SIZE) + base
    );
  }
  return cipher;
};
