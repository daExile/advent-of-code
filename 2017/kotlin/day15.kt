import java.io.File

class Generator(private val factor: Int) {
    private var value: Long = 0
    
    fun setValue(newValue: Long) {
        value = newValue
    }
    
    fun nextValue() = ((value * factor) % 2147483647).also { value = it }
    
    fun nextValueMultiple(n: Int): Long {
        var candidate: Long
        do candidate = nextValue() while (candidate % n != 0L)
        return candidate
    }
}

fun main() {
    val A = Generator(16807)
    val B = Generator(48271)
    val (a0, b0) = File("../__in/15.txt").readLines().map { Regex("""(\d+)""").find(it)!!.value.toLong() }
    
    var count1 = 0
    A.setValue(a0); B.setValue(b0)
    for (i in 1..40000000) if (A.nextValue() % 65536 == B.nextValue() % 65536) count1++
    println("Part 1: $count1")
    
    var count2 = 0
    A.setValue(a0); B.setValue(b0)
    for (i in 1..5000000) if (A.nextValueMultiple(4) % 65536 == B.nextValueMultiple(8) % 65536) count2++
    println("Part 2: $count2")
}