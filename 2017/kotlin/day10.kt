import java.io.File

fun rotateList(list: List<Int>, x: Int) = if (x == 0) list else list.subList(x.mod(list.size), list.size) + list.subList(0, x.mod(list.size))

fun reverseXinList(list: List<Int>, x: Int) = if (x in 1..list.size) list.subList(0, x).reversed() + list.subList(x, list.size) else list

fun knotHash(list: List<Int>, input: List<Int>, rounds: Int): List<Int> {
    var pos = 0; var skip = 0; var hashedList = list
    for (r in 1..rounds) for (n in input) {
            hashedList = rotateList(reverseXinList(hashedList, n), n + skip).also { pos = (pos + skip + n) % list.size; skip++ }
    }
    return rotateList(hashedList, -pos)
}

fun denseHash(sparseHash: List<Int>, format: (Int) -> String = { it -> String.format("%02x", it) }): String {
    var hash = ""
    for (i in sparseHash.chunked(16)) {
        var t = 0
        for (j in i) t = t.xor(j)
        hash += format(t)
    }
    return hash
}

fun main() {
    val input = File("10.txt").readText()
    val dataPart1 = input.split(",").mapNotNull { it.toIntOrNull() }
    val dataPart2 = input.map { it.code } + listOf(17, 31, 73, 47, 23)
    
    println("Part 1: ${with(knotHash(List(256) { i -> i }, dataPart1, 1)) { this[0] * this[1] }}")
    println("Part 2: ${denseHash(knotHash(List(256) { i -> i }, dataPart2, 64))}")
}