import java.io.File

fun main() {
    val almostRawInput = File("../__in/09.txt").readText().replace("!.".toRegex(), "")
    val cleanInput = almostRawInput.replace("<[^>]*>".toRegex(), "<>")

    var score = 0; var groupLevel = 0
    for (char in cleanInput) when (char) {
            '{' -> { groupLevel++; score += groupLevel }
            '}' -> groupLevel--
    }
    
    println("Part 1: $score")
    println("Part 2: ${almostRawInput.length - cleanInput.length}")
}