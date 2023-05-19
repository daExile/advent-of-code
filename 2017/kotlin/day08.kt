import java.io.File

fun op(operator: String, a: Int, b: Int): Boolean = when(operator) {
        "<=" -> a <= b
        ">=" -> a >= b
        "<" -> a < b
        ">" -> a > b
        "==" -> a == b
        else -> a != b
    }

fun main() {
    val registers = mutableMapOf<String, Int>()
    var maxvalue = 0
    for (line in File("08.txt").readLines()) {
        val (instruction, condition) = Regex("""(\w+) (\w+|[<>!=]=?) (-?\d+)""").findAll(line).map { it.value }.toList()
        val check = with(condition.split(" ")) { op(this[1], (registers[this[0]] ?: 0), this[2].toInt()) }
        if (check) with(instruction.split(" ")) {
            registers[this[0]] = (registers[this[0]] ?: 0) + (if (this[1] == "dec") -1 else 1) * this[2].toInt()
            if (registers[this[0]]!! > maxvalue) maxvalue = registers[this[0]]!!
        }
    }
    
    println("Part 1 answer: ${registers.values.max()}")
    println("Part 2 answer: $maxvalue")
}