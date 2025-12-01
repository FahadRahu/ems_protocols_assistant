/**
 * Code Timer Component
 * 
 * One-tap code start with interval announcements.
 * Per HPCPR protocol: 2-minute intervals.
 */

import { useState, useEffect, useCallback } from 'react';

interface CodeTimerProps {
  onIntervalComplete?: (intervalNumber: number) => void;
}

export function CodeTimer({ onIntervalComplete }: CodeTimerProps) {
  const [isRunning, setIsRunning] = useState(false);
  const [elapsedSeconds, setElapsedSeconds] = useState(0);
  const [intervalCount, setIntervalCount] = useState(0);

  const INTERVAL_SECONDS = 120; // 2 minutes

  const formatTime = (seconds: number): string => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleStart = () => {
    setIsRunning(true);
    setElapsedSeconds(0);
    setIntervalCount(0);
  };

  const handleStop = () => {
    setIsRunning(false);
  };

  useEffect(() => {
    if (!isRunning) return;

    const timer = setInterval(() => {
      setElapsedSeconds((prev) => {
        const newTime = prev + 1;
        
        // Check for interval completion
        if (newTime % INTERVAL_SECONDS === 0) {
          const newIntervalCount = Math.floor(newTime / INTERVAL_SECONDS);
          setIntervalCount(newIntervalCount);
          onIntervalComplete?.(newIntervalCount);
        }
        
        return newTime;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isRunning, onIntervalComplete]);

  return (
    <div className="bg-vp-dark rounded-lg p-6 text-center">
      <h2 className="text-xl font-semibold mb-4">Code Timer</h2>
      
      <div className="text-6xl font-mono font-bold text-white mb-4">
        {formatTime(elapsedSeconds)}
      </div>

      <div className="text-lg text-gray-400 mb-6">
        Interval: {intervalCount} | Next rotation in:{' '}
        {formatTime(INTERVAL_SECONDS - (elapsedSeconds % INTERVAL_SECONDS))}
      </div>

      {!isRunning ? (
        <button onClick={handleStart} className="btn-danger text-2xl px-12 py-4">
          🚨 START CODE
        </button>
      ) : (
        <button onClick={handleStop} className="btn-secondary text-xl">
          ⏹️ Stop Timer
        </button>
      )}
    </div>
  );
}
