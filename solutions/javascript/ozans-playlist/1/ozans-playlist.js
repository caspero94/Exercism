
export function removeDuplicates(playlist) {
  return Array.from(new Set(playlist))
}

/**
 * Checks whether a playlist includes a track.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {boolean} whether the track is in the playlist
 */
export function hasTrack(playlist, track) {
  const playClean = new Set(playlist)
  const x = playClean.size
  playClean.add(track)
  return x == playClean.size ? true : false
}

export function addTrack(playlist, track) {
  const playClean = new Set(playlist)
  playClean.add(track)
  return Array.from(playClean)
}

/**
 * Deletes a track from a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function deleteTrack(playlist, track) {
  const playClean = new Set(playlist)
  playClean.delete(track)
  return Array.from(playClean)
}

/**
 * Lists the unique artists in a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} list of artists
 */
export function listArtists(playlist) {
  return Array.from(new Set(playlist.map(c => c.split(" - ")[1])))
}
