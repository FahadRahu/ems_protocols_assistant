/**
 * Game Plan Component
 * 
 * Displays matched protocols and treatment steps.
 * Filters steps by user's certification level.
 */

import type { Protocol, ProviderLevel } from '../../types/protocol';

interface GamePlanProps {
  protocol: Protocol;
  userLevel: ProviderLevel;
}

export function GamePlan({ protocol, userLevel }: GamePlanProps) {
  // TODO: Implement protocol display with step filtering
  return (
    <div className="bg-vp-dark rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">{protocol.title}</h2>
      <div className="space-y-4">
        {protocol.steps.map((step) => (
          <div
            key={step.order}
            className="border-l-4 border-vp-accent pl-4 py-2"
          >
            <div className="flex items-center gap-2 mb-1">
              <span className="text-xs bg-vp-accent/20 text-vp-accent px-2 py-0.5 rounded">
                {step.provider_level}
              </span>
              <span className="text-sm text-gray-400">Step {step.order}</span>
            </div>
            <p className="text-white">{step.action}</p>
            {step.medication && (
              <p className="text-sm text-vp-success mt-1">
                💊 {step.medication.dose} {step.medication.route}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
