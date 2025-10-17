export function createAppointment(days, now = undefined) {
  now = !now ? new Date() : new Date(now)
  now.setDate(now.getDate() + days)
  return now
}

export function getAppointmentTimestamp(appointmentDate) {
  return appointmentDate.toISOString()
}

export function getAppointmentDetails(timestamp) {
  const ts = new Date(timestamp)
  return {"date": ts.getDate(), "hour" : ts.getHours(), "minute" : ts.getMinutes(), "month" : ts.getMonth(), "year" : ts.getFullYear()}
}

/**
 * Update an appointment with given options
 *
 * @param {string} timestamp (ISO 8601)
 * @param {Partial<Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>>} options
 *
 * @returns {Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>} the appointment details
 */
export function updateAppointment(timestamp, options) {
  timestamp = new Date(timestamp)
  for (let key in options) {
    let keyf = key == "year" ? "FullYear" : key == "hour" ? "hours" : key == "minute" ? "minutes" : key
    let setterName = `set${keyf.charAt(0).toUpperCase() + keyf.slice(1)}`;
    timestamp[setterName](options[key]);
  }
  return getAppointmentDetails(timestamp)
}

/**
 * Get available time in seconds (rounded) between two appointments
 *
 * @param {string} timestampA (ISO 8601)
 * @param {string} timestampB (ISO 8601)
 *
 * @returns {number} amount of seconds (rounded)
 */
export function timeBetween(timestampA, timestampB) {
  return Math.round((new Date(timestampB)-new Date(timestampA))/1000)
}

/**
 * Get available times between two appointment
 *
 * @param {string} appointmentTimestamp (ISO 8601)
 * @param {string} currentTimestamp (ISO 8601)
 */
export function isValid(appointmentTimestamp, currentTimestamp) {
  return new Date(appointmentTimestamp) - new Date(currentTimestamp) > 0 ? true : false
}
