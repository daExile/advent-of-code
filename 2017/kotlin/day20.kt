import java.io.File; import kotlin.math.floor; import kotlin.math.sqrt; import kotlin.math.sign

class MotionData(private val p: Int, private val v: Int, private val a: Int) : Comparable<MotionData> {
    override fun compareTo(other: MotionData) =
        if (a == other.a) if (v == other.v) p - other.p else v - other.v else a - other.a
    
    operator fun plus(other: MotionData) = MotionData(p + other.p, v + other.v, a + other.a)
    
    operator fun times(other: Int) = MotionData(p * other, v * other, a * other)
    
    fun sign() = if (a == 0) if (v == 0) p.sign else v.sign else a.sign
    
    // fun pAt(t: Int) = a * t * (t + 1) / 2 + v * t + p // remnant of another idea, may return to it
    
    fun solve(other: MotionData): Set<Int> {
        val diff = this + (other * -1)
        val a = diff.a
        val b = 2 * diff.v + a
        val c = 2 * diff.p
        
        if (a != 0) {
            with((b * b - 4 * a * c).toDouble()) {
                if (this < 0) return setOf()
                else return setOf((-b - sqrt(this)) / (2 * a), (-b + sqrt(this)) / (2 * a))
                        .filter { it == floor(it) && it > 0 }.map { it.toInt() }.toSet()
            }
        } else if (b != 0) {
            return setOf((-c / b).toDouble()).filter { it == floor(it) && it > 0 }.map { it.toInt() }.toSet()
        } else return if (c != 0) setOf() else setOf(0)
    }
}

class Particle(input: String) {
    val data: Array<MotionData>
    var collides = false

    init {
        with(Regex("""([-\d]+)""").findAll(input).map { it.value.toInt() }.toList()) { data = arrayOf(
                MotionData(this[0], this[3], this[6]),
                MotionData(this[1], this[4], this[7]),
                MotionData(this[2], this[5], this[8]) ) }
    }
    
    fun getAbsValue() = data[0] * data[0].sign() + data[1] * data[1].sign() + data[2] * data[2].sign()
    
    fun checkCollision(other: Particle) {
        var t = data[0].solve(other.data[0])
        if (t.isNotEmpty()) {
            t = t intersect data[1].solve(other.data[1])
            if (t.isNotEmpty()) {
                t = t intersect data[2].solve(other.data[2])
                if (t.isNotEmpty()) {
                    this.collides = true
                    other.collides = true
                }
            }
        }
    }
    
    // fun getPosAt(t: Int) = data.map { it.pAt(t) } // remnant of another idea, may return to it
}

fun main() {
    val GPUData = File("../__in/20.txt").readLines().map { Particle(it) }.toMutableList()
    println("Part 1: ${GPUData.indexOf(GPUData.minBy { it.getAbsValue() } )}")
    
    for (i in 0 until GPUData.lastIndex) {
        if (!GPUData[i].collides) for (j in i + 1..GPUData.lastIndex) {
            if (!GPUData[j].collides) GPUData[i].checkCollision(GPUData[j])
        }
    }
    println("Part 2: ${GPUData.filter { !it.collides }.size}")
}