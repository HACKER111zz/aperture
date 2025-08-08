import math

def solve_logarithmic_inequality():
    """
    Solve the inequality: log_{5-x}(x^2 - 6x + 9) <= 0
    """
    print("Solving: log_{5-x}(x² - 6x + 9) ≤ 0")
    print("=" * 60)
    
    # Step 1: Analyze domain restrictions
    print("Step 1: Domain Analysis")
    print("-" * 25)
    
    print("For the logarithm to be defined, we need:")
    print("1. Base condition: 5-x > 0 and 5-x ≠ 1")
    print("   → 5-x > 0  ⟹  x < 5")
    print("   → 5-x ≠ 1  ⟹  x ≠ 4")
    print("   Combined: x ∈ (-∞, 4) ∪ (4, 5)")
    
    print("\n2. Argument condition: x² - 6x + 9 > 0")
    
    # Step 2: Simplify the argument
    print("\nStep 2: Simplify the argument")
    print("-" * 35)
    
    print("x² - 6x + 9 = (x - 3)²")
    print("This is a perfect square trinomial.")
    print("\nSince (x - 3)² ≥ 0 for all real x:")
    print("• (x - 3)² > 0 when x ≠ 3")
    print("• (x - 3)² = 0 when x = 3")
    print("\nFor the logarithm to be defined, we need (x - 3)² > 0")
    print("Therefore: x ≠ 3")
    
    # Step 3: Combined domain
    print("\nStep 3: Combined Domain")
    print("-" * 30)
    print("Combining all restrictions:")
    print("• x < 5 (base > 0)")
    print("• x ≠ 4 (base ≠ 1)")
    print("• x ≠ 3 (argument > 0)")
    print("\nDomain: x ∈ (-∞, 3) ∪ (3, 4) ∪ (4, 5)")
    
    # Step 4: Solve the inequality
    print("\nStep 4: Solve the Inequality")
    print("-" * 35)
    
    print("The inequality is: log_{5-x}((x-3)²) ≤ 0")
    print("\nSince log_a(b) ≤ 0 means log_a(b) ≤ log_a(1):")
    print("• If a > 1: then b ≤ 1")
    print("• If 0 < a < 1: then b ≥ 1")
    
    print("\nCase 1: Base > 1")
    print("When 5-x > 1  ⟹  x < 4")
    print("Need: (x-3)² ≤ 1")
    print("This gives: |x-3| ≤ 1")
    print("So: -1 ≤ x-3 ≤ 1")
    print("Therefore: 2 ≤ x ≤ 4")
    print("Intersecting with x < 4 and x ≠ 3:")
    print("Solution for Case 1: x ∈ [2, 3) ∪ (3, 4)")
    
    print("\nCase 2: 0 < Base < 1")
    print("When 0 < 5-x < 1  ⟹  4 < x < 5")
    print("Need: (x-3)² ≥ 1")
    print("This gives: |x-3| ≥ 1")
    print("So: x-3 ≤ -1 or x-3 ≥ 1")
    print("Therefore: x ≤ 2 or x ≥ 4")
    print("Intersecting with 4 < x < 5:")
    print("Solution for Case 2: x ∈ (4, 5)")
    
    # Step 5: Final answer
    print("\nStep 5: Final Solution")
    print("-" * 25)
    print("Combining both cases:")
    print("Final Answer: x ∈ [2, 3) ∪ (3, 4) ∪ (4, 5)")
    
    return "x ∈ [2, 3) ∪ (3, 4) ∪ (4, 5)"

def verify_solution():
    """
    Verify the solution by testing specific values
    """
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    
    test_values = [1.5, 2, 2.5, 2.9, 3.1, 3.5, 4.1, 4.5, 4.9, 5.5]
    
    print(f"{'x':<6} {'Base':<8} {'Argument':<12} {'Log Value':<12} {'≤ 0?':<8} {'In Solution?'}")
    print("-" * 70)
    
    for val in test_values:
        base = 5 - val
        argument = (val - 3)**2
        
        # Check if in our solution set
        in_solution = ((2 <= val < 3) or (3 < val < 4) or (4 < val < 5))
        
        if base <= 0 or base == 1 or argument <= 0:
            status = "Undefined"
            log_val = "N/A"
            satisfies = "N/A"
        else:
            try:
                log_val = math.log(argument) / math.log(base)
                satisfies = "Yes" if log_val <= 0 else "No"
                log_val = f"{log_val:.3f}"
            except:
                status = "Error"
                log_val = "N/A"
                satisfies = "N/A"
        
        if base <= 0 or base == 1:
            base_str = f"{base:.1f}*"
        else:
            base_str = f"{base:.1f}"
            
        in_sol_str = "Yes" if in_solution else "No"
        
        print(f"{val:<6} {base_str:<8} {argument:<12.1f} {log_val:<12} {satisfies:<8} {in_sol_str}")
    
    print("\n* Base is invalid (≤0 or =1)")

def create_summary():
    """
    Create a mathematical summary
    """
    print("\n" + "=" * 60)
    print("MATHEMATICAL SUMMARY")
    print("=" * 60)
    
    print("Original inequality: log_{5-x}(x² - 6x + 9) ≤ 0")
    print("\nKey steps:")
    print("1. Factor argument: x² - 6x + 9 = (x - 3)²")
    print("2. Domain restrictions:")
    print("   • Base: 5-x > 0 and 5-x ≠ 1  ⟹  x ∈ (-∞,4) ∪ (4,5)")
    print("   • Argument: (x-3)² > 0  ⟹  x ≠ 3")
    print("   • Combined: x ∈ (-∞,3) ∪ (3,4) ∪ (4,5)")
    print("\n3. Case analysis:")
    print("   • Case 1 (x < 4): (x-3)² ≤ 1  ⟹  x ∈ [2,3) ∪ (3,4)")
    print("   • Case 2 (4 < x < 5): (x-3)² ≥ 1  ⟹  x ∈ (4,5)")
    print("\nFINAL ANSWER: x ∈ [2, 3) ∪ (3, 4) ∪ (4, 5)")

if __name__ == "__main__":
    solution = solve_logarithmic_inequality()
    verify_solution()
    create_summary()