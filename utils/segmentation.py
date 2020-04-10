import numpy as np
import matplotlib.pyplot as plt


class SignalML:
    def __init__(self, data, peak):
        self.data = data
        self.peak = peak

    def SegmentWindow(self):
        '''
        segment in specipic window.
        '''
        signals = []
        for i in range(1, len(self.peak) - 1):  # fixed window size
            diff1 = abs(self.peak[i] - 70)  # previous 70
            diff2 = abs(self.peak[i] + 100)  # after 100
            signal = self.data[diff1:diff2]
            signals.append(signal)

    def SegmentPreAfter(self):
        '''
        Segment with reference to before and after peak
        '''
        count = 1
        signals = []
        for i in self.peak[1:-1]:
            diff1 = abs(self.peak[count - 1] - i)
            diff2 = abs(self.peak[count + 1] - i)
            previous = self.peak[count - 1] + diff1 // 2
            after = self.peak[count + 1] - diff2 // 2
            signal = self.data[previous:after]
            signals.append(signal)
            count += 1
        return signals


class SignalV:
    def __init__(self, data, peak):
        self.data = data
        self.peak = peak

    def SegmentWindow(self):
        signals = []
        for i in range(1, len(self.peak) - 1):
            diff1 = abs(self.peak[i] - 70)
            diff2 = abs(self.peak[i] + 100)
            signal = self.data[diff1:diff2]
            signals.append(signal)
        return signals

    def SegmentPreAfter(self):
        count = 1
        signals = []
        for i in self.peak[1:-1]:
            diff1 = abs(self.peak[count - 1] - i)
            diff2 = abs(self.peak[count + 1] - i)
            previous = self.peak[count - 1] + diff1 // 2
            after = self.peak[count + 1] - diff2 // 2
            signal = self.data[previous:after]
            signals.append(signal)
            count += 1
        return signals