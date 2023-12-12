import java.io.File

open class Thread {
    var registers = mutableMapOf<String, Long>()
    var pointer = 0
    var wait = false // *sigh* backported for easier check, needs work
    
    fun getVal(x: String) = x.toLongOrNull() ?: (registers[x]) ?: 0L
    
    open fun _snd(x: String) { pointer++; registers["snd"] = getVal(x) }
    open fun _rcv(x: String) { if (getVal(x) != 0L) registers["rcv"] = getVal("snd").also { pointer = -1 } else pointer++ }
    fun _set(x: String, y: String) { pointer++; registers[x] = getVal(y) }
    fun _add(x: String, y: String) { pointer++; registers[x] = getVal(x) + getVal(y) }
    fun _mul(x: String, y: String) { pointer++; registers[x] = getVal(x) * getVal(y) }
    fun _mod(x: String, y: String) { pointer++; registers[x] = getVal(x) % getVal(y) }
    fun _jgz(x: String, y: String) { if (getVal(x) > 0) pointer += getVal(y).toInt() else pointer++ }
}

class ThreadDuet(id: Long, val queueIn: ArrayDeque<Long>, val queueOut: ArrayDeque<Long>) : Thread() {
    init { registers["p"] = id }
    
    override fun _snd(x: String) { queueOut.addFirst(getVal(x)); registers["snd"] = getVal("snd") + 1; pointer++ }
    override fun _rcv(x: String) {
        if (!queueIn.isEmpty()) { registers[x] = queueIn.removeLast(); wait = false; pointer++ }
        else wait = true
    }
}

fun main() {
    val input = File("../__in/18.txt").readLines().map { it.split(" ") }
    val queue0 = ArrayDeque<Long>(); val queue1 = ArrayDeque<Long>()
    val threads = listOf(Thread(), ThreadDuet(0, queue0, queue1), ThreadDuet(1, queue1, queue0))
    // run them all! p1 --^  p2 program "0" --^             p2 program "1" --^
    var liveThreads: Int
    do {
        liveThreads = 0
        for (item in threads) {
            if (item.pointer in input.indices) {
                val cmd = input[item.pointer]
                when (cmd[0]) {
                    "snd" -> item._snd(cmd[1])
                    "rcv" -> item._rcv(cmd[1])
                    "set" -> item._set(cmd[1], cmd[2])
                    "add" -> item._add(cmd[1], cmd[2])
                    "mul" -> item._mul(cmd[1], cmd[2])
                    "mod" -> item._mod(cmd[1], cmd[2])
                    "jgz" -> item._jgz(cmd[1], cmd[2])
                }
                if (!item.wait) liveThreads++
            }
        }
    } while (liveThreads > 0)
    
    println("Part 1: ${threads[0].registers["rcv"]}")
    println("Part 2: ${threads[2].registers["snd"]}")
}