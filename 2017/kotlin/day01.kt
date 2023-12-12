import java.io.File

fun main() {
    val input = File("../__in/01.txt").readText().trim()
    val list = input.map { it.toString().toInt() }
    var checksum = 0
    
    // part 1
    for (i in list.indices) if (list[i] == list[(i + 1) % list.size]) checksum += list[i]
    println("Part 1: $checksum")
    
    // part 2
    checksum = 0
    for (i in list.indices) if (list[i] == list[(i + list.size / 2) % list.size]) checksum += list[i]
    println("Part 2: $checksum")
}