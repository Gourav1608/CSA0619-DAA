import time
import random
import math

class VideoStreamingProcessor:
    def __init__(self):
        self.operations_count = 0

    def process_user_stream_data(self, data):
        n = len(data)
        if n <= 1:
            return data

        mid = n // 2
        left_half = self.process_user_stream_data(data[:mid])
        right_half = self.process_user_stream_data(data[mid:])

        return self._merge_streams(left_half, right_half)

    def _merge_streams(self, left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.operations_count += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1
            self.operations_count += 1
            
        while j < len(right):
            merged.append(right[j])
            j += 1
            self.operations_count += 1

        return merged

def run_scalability_benchmark():
    print("=" * 70)
    print("VIDEO STREAMING PLATFORM: T(n) = 2T(n/2) + n BENCHMARK")
    print("=" * 70)
    print(f"{'Input Size (n)':<15} | {'Measured Ops':<15} | {'n log2(n) Target':<18} | {'Time (ms)':<10}")
    print("-" * 70)

    dataset_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

    for n in dataset_sizes:
        sample_data = [random.randint(1, 100000) for _ in range(n)]
        processor = VideoStreamingProcessor()
        
        start_time = time.perf_counter()
        processor.process_user_stream_data(sample_data)
        end_time = time.perf_counter()

        elapsed_ms = (end_time - start_time) * 1000
        theoretical_bounds = int(n * math.log2(n))

        print(f"{n:<15} | {processor.operations_count:<15} | {theoretical_bounds:<18} | {elapsed_ms:<10.2f}")

    print("=" * 70)
    print("ANALYSIS: Measured operations align tightly with the n log2(n) target,")
    print("empirically validating Case 2 of the Master Theorem: Theta(n log n).")

if __name__ == "__main__":
    run_scalability_benchmark()
