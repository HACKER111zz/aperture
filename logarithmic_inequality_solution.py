import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, log, simplify, factor, expand
from sympy.plotting import plot
import sympy as sp

def solve_logarithmic_inequality():
    """
    Solve the inequality: log_{5-x}(x^2 - 6x + 9) <= 0
    """
    print("Solving: log_{5-x}(x^2 - 6x + 9) ≤ 0")
    print("=" * 50)
    
    x = symbols('x', real=True)
    
    # Step 1: Analyze domain restrictions
    print("Step 1: Domain Analysis")
    print("-" * 20)
    
    # For logarithm to be defined:
    # 1. Base must be positive and ≠ 1: 5-x > 0 and 5-x ≠ 1
    # 2. Argument must be positive: x^2 - 6x + 9 > 0
    
    print("Domain restrictions:")
    print("1. Base condition: 5-x > 0 and 5-x ≠ 1")
    print("   → x < 5 and x ≠ 4")
    print("   → x ∈ (-∞, 4) ∪ (4, 5)")
    
    # Step 2: Simplify the argument
    print("\nStep 2: Simplify the argument")
    print("-" * 30)
    
    argument = x**2 - 6*x + 9
    factored_argument = factor(argument)
    print(f"x² - 6x + 9 = {factored_argument}")
    print("This is a perfect square: (x - 3)²")
    
    # Since (x-3)² ≥ 0 for all real x, and (x-3)² = 0 only when x = 3
    print("\nArgument analysis:")
    print("(x - 3)² > 0 for all x ≠ 3")
    print("(x - 3)² = 0 when x = 3")
    print("Since we need the argument > 0 for log to be defined, x ≠ 3")
    
    # Step 3: Combine domain restrictions
    print("\nStep 3: Combined domain")
    print("-" * 25)
    print("Combining all restrictions:")
    print("x ∈ (-∞, 4) ∪ (4, 5) and x ≠ 3")
    print("Final domain: x ∈ (-∞, 3) ∪ (3, 4) ∪ (4, 5)")
    
    # Step 4: Solve the inequality
    print("\nStep 4: Solve log_{5-x}((x-3)²) ≤ 0")
    print("-" * 40)
    
    print("For logarithmic inequality log_a(b) ≤ 0:")
    print("This means log_a(b) ≤ log_a(1), so b ≤ 1 if a > 1, or b ≥ 1 if 0 < a < 1")
    
    # Case 1: Base > 1 (5-x > 1, so x < 4)
    print("\nCase 1: Base > 1 (5-x > 1, so x < 4)")
    print("When x < 4: (x-3)² ≤ 1")
    print("This gives: |x-3| ≤ 1")
    print("So: -1 ≤ x-3 ≤ 1")
    print("Therefore: 2 ≤ x ≤ 4")
    print("Combined with x < 4 and x ≠ 3: x ∈ [2, 3) ∪ (3, 4)")
    
    # Case 2: 0 < Base < 1 (0 < 5-x < 1, so 4 < x < 5)
    print("\nCase 2: 0 < Base < 1 (0 < 5-x < 1, so 4 < x < 5)")
    print("When 4 < x < 5: (x-3)² ≥ 1")
    print("This gives: |x-3| ≥ 1")
    print("So: x-3 ≤ -1 or x-3 ≥ 1")
    print("Therefore: x ≤ 2 or x ≥ 4")
    print("Combined with 4 < x < 5: x ∈ (4, 5)")
    
    # Step 5: Final solution
    print("\nStep 5: Final Solution")
    print("-" * 20)
    print("Combining both cases:")
    print("Case 1: x ∈ [2, 3) ∪ (3, 4)")
    print("Case 2: x ∈ (4, 5)")
    print("\nFinal answer: x ∈ [2, 3) ∪ (3, 4) ∪ (4, 5)")
    
    return [2, 3), (3, 4), (4, 5)

def verify_solution():
    """
    Verify the solution by testing specific values
    """
    print("\n" + "=" * 50)
    print("VERIFICATION")
    print("=" * 50)
    
    test_values = [1.5, 2, 2.5, 3.5, 4.5, 5.5]
    
    for val in test_values:
        try:
            base = 5 - val
            if base <= 0 or base == 1:
                result = "Undefined (invalid base)"
            else:
                argument = (val - 3)**2
                if argument <= 0:
                    result = "Undefined (invalid argument)"
                else:
                    log_value = np.log(argument) / np.log(base)
                    result = f"≈ {log_value:.3f}, {'✓' if log_value <= 0 else '✗'}"
        except:
            result = "Undefined"
        
        print(f"x = {val}: log_{{{5-val}}}({(val-3)**2:.1f}) {result}")

def plot_function():
    """
    Plot the function to visualize the solution
    """
    print("\n" + "=" * 50)
    print("GRAPHICAL ANALYSIS")
    print("=" * 50)
    
    x_vals = np.linspace(0, 6, 1000)
    y_vals = []
    
    for x in x_vals:
        base = 5 - x
        argument = (x - 3)**2
        
        if base > 0 and base != 1 and argument > 0:
            try:
                y = np.log(argument) / np.log(base)
                y_vals.append(y)
            except:
                y_vals.append(np.nan)
        else:
            y_vals.append(np.nan)
    
    plt.figure(figsize=(12, 8))
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='log_{5-x}((x-3)²)')
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.7, label='y = 0')
    plt.axvline(x=3, color='g', linestyle=':', alpha=0.7, label='x = 3 (undefined)')
    plt.axvline(x=4, color='g', linestyle=':', alpha=0.7, label='x = 4 (undefined)')
    plt.axvline(x=5, color='g', linestyle=':', alpha=0.7, label='x = 5 (undefined)')
    
    # Highlight solution regions
    plt.axvspan(2, 3, alpha=0.3, color='yellow', label='Solution: [2,3)')
    plt.axvspan(3, 4, alpha=0.3, color='yellow', label='Solution: (3,4)')
    plt.axvspan(4, 5, alpha=0.3, color='yellow', label='Solution: (4,5)')
    
    plt.xlim(0, 6)
    plt.ylim(-3, 3)
    plt.xlabel('x')
    plt.ylabel('log_{5-x}((x-3)²)')
    plt.title('Graph of log_{5-x}((x-3)²) ≤ 0')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/workspace/logarithmic_inequality_graph.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Graph saved as 'logarithmic_inequality_graph.png'")

if __name__ == "__main__":
    solve_logarithmic_inequality()
    verify_solution()
    plot_function()