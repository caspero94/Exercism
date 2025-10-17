// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */


export function Size(width = 80, height = 60) {
  this.width = width
  this.height = height
}

Size.prototype.resize = function (width, height){
  this.width = width
  this.height = height
}

export function Position(x=0, y=0) {
  this.x = x
  this.y = y
}

Position.prototype.move = function (x, y){
  this.x = x
  this.y = y
}

export class ProgramWindow {
  constructor() {
    this.screenSize = new Size(800,600)
    this.size = new Size()
    this.position = new Position()
  }
  resize (newSize){

    const copyNewSize = new Size(newSize.width, newSize.height)

    if (copyNewSize.width < 1) copyNewSize.width = 1
    if (copyNewSize.height < 1) copyNewSize.height = 1

    const maxWidth = this.screenSize.width - this.position.x
    const maxHeight = this.screenSize.height - this.position.y

    if (copyNewSize.width > maxWidth) copyNewSize.width = maxWidth
    if (copyNewSize.height > maxHeight) copyNewSize.height = maxHeight
    
    this.size = copyNewSize
  }
  move (newPosition){
    
    const copyNewPos = new Position(newPosition.x, newPosition.y)
    if (copyNewPos.x < 0) copyNewPos.x = 0
    if (copyNewPos.y < 0) copyNewPos.y = 0
    if (copyNewPos.x > this.screenSize.width - this.size.width) copyNewPos.x = this.screenSize.width - this.size.width
    if (copyNewPos.y > this.screenSize.height - this.size.height) copyNewPos.y = this.screenSize.height - this.size.height
    
    this.position = copyNewPos
  }
  
}

export function changeWindow(programWindow){
  programWindow.resize(new Size(400,300))
  programWindow.move(new Position(100,150))
  return programWindow
}