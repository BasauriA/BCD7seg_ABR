# Cocotb's GDS gate-level test runner runs with GATES=yes. The decoder is
# combinational, therefore the testbench intentionally does not generate a clock.
import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    dut.ena.value = 1
    dut.uio_in.value = 0
    dut.rst_n.value = 1

    expected = [
        0x3F, 0x06, 0x5B, 0x4F, 0x66,
        0x6D, 0x7D, 0x07, 0x7F, 0x6F,
    ]

    for digit, encoded in enumerate(expected):
        dut.ui_in.value = digit
        await Timer(1, unit="ns")
        assert int(dut.uo_out.value) == encoded, (
            f"BCD digit {digit}: expected 0x{encoded:02x}, "
            f"got 0x{int(dut.uo_out.value):02x}"
        )

    for digit in range(10, 16):
        dut.ui_in.value = digit
        await Timer(1, unit="ns")
        assert int(dut.uo_out.value) == 0, (
            f"Invalid BCD digit {digit} should blank the display"
        )
