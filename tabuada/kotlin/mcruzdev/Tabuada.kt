fun main() {
    tabuadaDe(140)
}

fun tabuadaDe(numero: Int) {
    for (contador in 1 until 11) {
        println("$contador * $numero = ${contador * numero}")
    }
}