@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 1

    # Test digits 0 through 9.
    expected = [0x3F, 0x06, 0x5B, 0x4F, 0x66,
                0x6D, 0x7D, 0x07, 0x7F, 0x6F]

    for digit, encoded in enumerate(expected):
        dut.ui_in.value = digit
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == encoded
