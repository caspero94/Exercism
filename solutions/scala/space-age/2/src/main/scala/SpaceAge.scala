object SpaceAge {

  private val EARTH_SECONDS = 31557600.0

  private def calculate(orbitPeriod: Double) =
    (seconds: Double) => seconds / EARTH_SECONDS / orbitPeriod

  val onEarth = calculate(1.0)
  val onMercury = calculate(0.2408467)
  val onVenus = calculate(0.61519726)
  val onMars = calculate(1.8808158)
  val onJupiter = calculate(11.862615)
  val onSaturn = calculate(29.447498)
  val onUranus = calculate(84.016846)
  val onNeptune = calculate(164.79132)

}
