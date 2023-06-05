import java.io.File

fun main() {
    var progs = mutableListOf("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p")
    val dance = File("16.txt")
        .readText().split(",")
        .map { listOf(it[0].toString()) + it.substring(1).split("/") }

    val log = mutableMapOf<Int, String>()
    var round = 0
    do {
        log[round] = progs.joinToString("")
        round++
        for (step in dance) when (step[0]) {
            "s" -> progs = rotateList(progs, -step[1].toInt()).toMutableList()
            "p" -> progs[progs.indexOf(step[1])] = progs[progs.indexOf(step[2])]
                .also { progs[progs.indexOf(step[2])] = progs[progs.indexOf(step[1])] }
            "x" -> progs[step[1].toInt()] = progs[step[2].toInt()]
                .also { progs[step[2].toInt()] = progs[step[1].toInt()] }
        }
    } while(progs.joinToString("") !in log.values)
    
    val target = 1000000000 % round
    println("Part 1: ${log[1]}")
    println("Part 2: ${log[target]}")
}