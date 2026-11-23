/*
 * Copyright (c) 2026 Alexander Basauri Romero
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

  // Map the lower four input pins to a seven-segment display.
  // Output bits 0-6 are segments A-G (active high).
  reg [6:0] segments;

  always @* begin
    case (ui_in[3:0])
      4'h0: segments = 7'b0111111; // 0
      4'h1: segments = 7'b0000110; // 1
      4'h2: segments = 7'b1011011; // 2
      4'h3: segments = 7'b1001111; // 3
      4'h4: segments = 7'b1100110; // 4
      4'h5: segments = 7'b1101101; // 5
      4'h6: segments = 7'b1111101; // 6
      4'h7: segments = 7'b0000111; // 7
      4'h8: segments = 7'b1111111; // 8
      4'h9: segments = 7'b1101111; // 9
      default: segments = 7'b0000000;
    endcase
  end

  assign uo_out  = {1'b0, segments};
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  // List unused inputs to prevent warnings.
  wire _unused = &{uio_in, ena, clk, rst_n, 1'b0};

endmodule
