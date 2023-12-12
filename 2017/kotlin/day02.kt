import java.io.File

fun findPairAndDivide(list: List<Int>): Int {
    for (i in 0..list.lastIndex - 1) {
        for (j in (i + 1)..list.lastIndex) {
            if (list[j] % list[i] == 0) return list[j] / list[i]
        }
    }
    return 0
}

fun main() {
    val input = File("../__in/02.txt").readLines()
    
    var checksum1 = 0
    var checksum2 = 0
    
    for (line in input) {
        val list = line.split("""\s+""".toRegex()).map { it.toInt() }.sorted()
        checksum1 += list.last() - list.first()
        checksum2 += findPairAndDivide(list)
    }
    
    println("Part 1: $checksum1")
    println("Part 2: $checksum2")
}