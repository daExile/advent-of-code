import java.io.File

fun main() {
    val input = File("../__in/10.txt").readText().trim()
    val dataPart1 = input.split(",").mapNotNull { it.toIntOrNull() }
    val dataPart2 = input.map { it.code } + listOf(17, 31, 73, 47, 23)
    
    println("Part 1: ${with(knotHash(List(256) { i -> i }, dataPart1, 1)) { this[0] * this[1] }}")
    println("Part 2: ${denseHash(knotHash(List(256) { i -> i }, dataPart2, 64))}")
}