// convenience
operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>) = Pair(this.first + other.first, this.second + other.second)

// knot hashing
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