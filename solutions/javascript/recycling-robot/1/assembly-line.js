
import { ElectronicDevice } from './lib.js';


export function isBoolean(value) {
  return typeof value == "boolean"
}


export function isNumber(value) {
  return typeof value === "number" && Number.isFinite(value) || typeof value === "bigint"
}

export function isObject(value) {
  if (value === null) return false
  return typeof value === "object" 
}

export function isNumericString(value) {
  if (typeof value !== "string") return false;
  if (/^-?\d+$/.test(value)) return true;
  return false;
}

export function isElectronic(object) {
  return object instanceof ElectronicDevice
}

export function isNonEmptyArray(value) {
  if (value == null) return false
  return value.length > 0 & Array.isArray(value) ? true : false
}

export function isEmptyArray(value) {
  if (Array.isArray(value) == false) return false
  return value.length == 0 ? true : false
}

export function hasType(object) {
  return "type" in object
}

export function assertHasId(object) {
  if ("id" in object) return undefined
  throw new Error("Object is missing the 'id' property");
}

export function hasIdProperty(object) {
  return Object.hasOwn(object, "id")
}

export function hasDefinedType(object) {
  return object.hasOwnProperty('type') && object.type !== undefined
}
