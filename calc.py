# -*- coding: utf-8 -*-
import math

def calculate_pipe(q_liters, diameter_mm, length_m):
    Q = q_liters / 1000.0
    D = diameter_mm / 1000.0
    area = math.pi * (D ** 2) / 4.0
    velocity = Q / area
    C = 150
    hf = 10.67 * length_m * (Q ** 1.852) / ((C ** 1.852) * (D ** 4.87))
    return velocity, hf

if __name__ == "__main__":
    print("--- Pipe Hydraulics Calculator ---")
    q = 10.0
    d = 100.0
    l = 500.0
    v, head_loss = calculate_pipe(q, d, l)
    print(f"Velocity: {v:.2f} m/s")
    print(f"Head Loss: {head_loss:.2f} m")
  
