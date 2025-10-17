
export function isValidCommand(command) {
  return /^chatbot/i.test(command)
}

export function removeEmoji(message) {
  return message = message.replace(new RegExp(/emoji\d+/,'gi'), "")
}

export function checkPhoneNumber(number) {
  return /\(\+\d\d\)\s\d\d\d-\d\d\d-\d\d\d/.test(number) ? "Thanks! You can now download me to your phone." : `Oops, it seems like I can't reach out to ${number}`
}

export function getURL(userInput) {
  return userInput.match(/\b\w+.(?:com|so)\b/g)
}

export function niceToMeetYou(fullName) {
  return `Nice to meet you, ${fullName.split(", ")[1]} ${fullName.split(", ")[0]}`
}
