object Leap {
  def leapYear(year: Int): Boolean = {
    val isDivisible4 = year % 4 == 0
    val isDivisible100 = year % 100 == 0
    val isDivisible400 = year % 400 == 0
    isDivisible4 && !isDivisible100 || isDivisible400
  }
}
