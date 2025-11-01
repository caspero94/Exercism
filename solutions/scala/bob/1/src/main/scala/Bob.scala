object Bob {
  def response(statement: String): String =

    val cleanStatement: String = statement.trim

    def esSilencio(s: String): Boolean = s.length == 0
    def esGrito(s: String): Boolean =
      val letras = s.filter(_.isLetter)
      letras.nonEmpty && letras.forall(_.isUpper)
    def esPregunta(s: String): Boolean = s.last == '?'

    cleanStatement match {
      case s if esSilencio(s) => "Fine. Be that way!"
      case s if esGrito(s) && esPregunta(s) =>
        "Calm down, I know what I'm doing!"
      case s if esGrito(s)    => "Whoa, chill out!"
      case s if esPregunta(s) => "Sure."
      case _                  => "Whatever."
    }
}
