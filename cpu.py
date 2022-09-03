import pyarrow

# 4KB (4096 bytes) of memory
# 16 8-bit registers
# A 16-bit register (this.i) to store memory addresses
# Two timers. One for the delay, and one for the sound.
# A program counter that stores the address currently being executed
# An array to represent the stack


sprites = [
    0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
    0x20, 0x60, 0x20, 0x20, 0x70,  # 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
    0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
    0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
    0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
    0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
    0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
    0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
    0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
    0xF0, 0x80, 0xF0, 0x80, 0x80   # F
]

# 4KB (4096 bytes) of memory
memory = pyarrow.UInt8Array(4096)

# 16 8-bit registers
v = [0] * 16

# Stores memory addresses. Set this to 0 since we aren't storing anything at initialization.
i = 0

# Timers
delayTimer = 0
soundTimer = 0

# Program counter. Stores the currently executing address.
pc = 0x200

# Don't initialize this with a size in order to avoid empty results.
stack = []

# Some instructions require pausing, such as Fx0A.
paused = False

speed = 10

i = 0
loc = 0


def cpu():

    if i < sprites.length:
        i + 1
        memory[i] = sprites[i]


def loadprogram(program):
    if loc < program.length:
        memory[0x200 + loc] = program[loc]


def loadRom(romName):
            let program = new Uint8Array(request.response)

            # Load the ROM/program into memory
            loadProgramIntoMemory(program)

    # Initialize a GET request to retrieve the ROM from our roms folder
    request.open('GET', 'roms/' + romName);
    request.responseType = 'arraybuffer';

    # Send the GET request
    request.send();
}