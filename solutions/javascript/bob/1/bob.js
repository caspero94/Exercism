//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


/* 
  Si termina en  "?" -> Sure.
  Si esta todo en mayusculas. -> Whoa, chill out!
  Termina en exclamacion sin mayus "!" -> Calm down, I know what I'm doing!
  Para el silencio, espacios -> Fine. Be that way
  Cualquier otra cosa Whatever
*/

export const hey = (message) => {

  if (!message.trim()) return 'Fine. Be that way!'

  const allUpper = /[A-Z]/.test(message) && !/[a-z]/.test(message)
  const question = message.trim().slice(-1) === '?'

  if (allUpper && question) return "Calm down, I know what I'm doing!"
  else if (question) return 'Sure.'
  else if (allUpper) return 'Whoa, chill out!'
  else return 'Whatever.'
};
