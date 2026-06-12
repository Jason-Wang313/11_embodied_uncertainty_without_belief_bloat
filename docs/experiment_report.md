# Experiment Report

## Setup
- Episodes per setting: 2000
- Nuisance bits: [0, 2, 4, 8, 16, 32]
- Hidden task mode selects which route succeeds; nuisance bits never affect route costs.
- TAO keeps the contested action edge set; the entropy baseline keeps a full factored belief and senses while total entropy remains above threshold.

## Key Result
TAO commits immediately when task mode is known, no matter how many nuisance bits remain unknown. In decision-ambiguous states, TAO inspects the task mode once and then commits. The entropy baseline scans nuisance bits because they dominate generic uncertainty.

## Summary Table
| Scenario | Nuisance bits | Policy | Mean cost | Success | Nuisance senses | Max belief states | Mean TAO edges |
|---|---:|---|---:|---:|---:|---:|---:|
| decision_ambiguous | 0 | entropy_threshold | 2.000 | 1.000 | 0.000 | 2.0 | 0.500 |
| decision_ambiguous | 0 | qmdp | 6.786 | 0.474 | 0.000 | 2.0 | 1.000 |
| decision_ambiguous | 0 | tao | 2.000 | 1.000 | 0.000 | 2.0 | 0.500 |
| decision_ambiguous | 0 | voi_oracle | 2.000 | 1.000 | 0.000 | 2.0 | 0.500 |
| decision_ambiguous | 2 | entropy_threshold | 2.400 | 1.000 | 2.000 | 8.0 | 0.750 |
| decision_ambiguous | 2 | qmdp | 6.500 | 0.500 | 0.000 | 8.0 | 1.000 |
| decision_ambiguous | 2 | tao | 2.000 | 1.000 | 0.000 | 8.0 | 0.500 |
| decision_ambiguous | 2 | voi_oracle | 2.000 | 1.000 | 0.000 | 8.0 | 0.500 |
| decision_ambiguous | 4 | entropy_threshold | 2.800 | 1.000 | 4.000 | 32.0 | 0.833 |
| decision_ambiguous | 4 | qmdp | 6.258 | 0.522 | 0.000 | 32.0 | 1.000 |
| decision_ambiguous | 4 | tao | 2.000 | 1.000 | 0.000 | 32.0 | 0.500 |
| decision_ambiguous | 4 | voi_oracle | 2.000 | 1.000 | 0.000 | 32.0 | 0.500 |
| decision_ambiguous | 8 | entropy_threshold | 3.600 | 1.000 | 8.000 | 512.0 | 0.900 |
| decision_ambiguous | 8 | qmdp | 6.373 | 0.511 | 0.000 | 512.0 | 1.000 |
| decision_ambiguous | 8 | tao | 2.000 | 1.000 | 0.000 | 512.0 | 0.500 |
| decision_ambiguous | 8 | voi_oracle | 2.000 | 1.000 | 0.000 | 512.0 | 0.500 |
| decision_ambiguous | 16 | entropy_threshold | 5.200 | 1.000 | 16.000 | 131072.0 | 0.944 |
| decision_ambiguous | 16 | qmdp | 6.280 | 0.520 | 0.000 | 131072.0 | 1.000 |
| decision_ambiguous | 16 | tao | 2.000 | 1.000 | 0.000 | 131072.0 | 0.500 |
| decision_ambiguous | 16 | voi_oracle | 2.000 | 1.000 | 0.000 | 131072.0 | 0.500 |
| decision_ambiguous | 32 | entropy_threshold | 8.400 | 1.000 | 32.000 | 8589934592.0 | 0.971 |
| decision_ambiguous | 32 | qmdp | 6.439 | 0.505 | 0.000 | 8589934592.0 | 1.000 |
| decision_ambiguous | 32 | tao | 2.000 | 1.000 | 0.000 | 8589934592.0 | 0.500 |
| decision_ambiguous | 32 | voi_oracle | 2.000 | 1.000 | 0.000 | 8589934592.0 | 0.500 |
| nuisance_only | 0 | entropy_threshold | 1.000 | 1.000 | 0.000 | 1.0 | 0.000 |
| nuisance_only | 0 | qmdp | 1.000 | 1.000 | 0.000 | 1.0 | 0.000 |
| nuisance_only | 0 | tao | 1.000 | 1.000 | 0.000 | 1.0 | 0.000 |
| nuisance_only | 0 | voi_oracle | 1.000 | 1.000 | 0.000 | 1.0 | 0.000 |
| nuisance_only | 2 | entropy_threshold | 1.400 | 1.000 | 2.000 | 4.0 | 0.000 |
| nuisance_only | 2 | qmdp | 1.000 | 1.000 | 0.000 | 4.0 | 0.000 |
| nuisance_only | 2 | tao | 1.000 | 1.000 | 0.000 | 4.0 | 0.000 |
| nuisance_only | 2 | voi_oracle | 1.000 | 1.000 | 0.000 | 4.0 | 0.000 |
| nuisance_only | 4 | entropy_threshold | 1.800 | 1.000 | 4.000 | 16.0 | 0.000 |
| nuisance_only | 4 | qmdp | 1.000 | 1.000 | 0.000 | 16.0 | 0.000 |
| nuisance_only | 4 | tao | 1.000 | 1.000 | 0.000 | 16.0 | 0.000 |
| nuisance_only | 4 | voi_oracle | 1.000 | 1.000 | 0.000 | 16.0 | 0.000 |
| nuisance_only | 8 | entropy_threshold | 2.600 | 1.000 | 8.000 | 256.0 | 0.000 |
| nuisance_only | 8 | qmdp | 1.000 | 1.000 | 0.000 | 256.0 | 0.000 |
| nuisance_only | 8 | tao | 1.000 | 1.000 | 0.000 | 256.0 | 0.000 |
| nuisance_only | 8 | voi_oracle | 1.000 | 1.000 | 0.000 | 256.0 | 0.000 |
| nuisance_only | 16 | entropy_threshold | 4.200 | 1.000 | 16.000 | 65536.0 | 0.000 |
| nuisance_only | 16 | qmdp | 1.000 | 1.000 | 0.000 | 65536.0 | 0.000 |
| nuisance_only | 16 | tao | 1.000 | 1.000 | 0.000 | 65536.0 | 0.000 |
| nuisance_only | 16 | voi_oracle | 1.000 | 1.000 | 0.000 | 65536.0 | 0.000 |
| nuisance_only | 32 | entropy_threshold | 7.400 | 1.000 | 32.000 | 4294967296.0 | 0.000 |
| nuisance_only | 32 | qmdp | 1.000 | 1.000 | 0.000 | 4294967296.0 | 0.000 |
| nuisance_only | 32 | tao | 1.000 | 1.000 | 0.000 | 4294967296.0 | 0.000 |
| nuisance_only | 32 | voi_oracle | 1.000 | 1.000 | 0.000 | 4294967296.0 | 0.000 |

## Plot Status
- `results/cost_nuisance_only.pdf`
- `results/cost_decision_ambiguous.pdf`
- `results/representation_bloat.pdf`
