# PedDesignGPT Quick-Start

Welcome to PedDesignGPT, a pediatric radiologist AI chatbot designed to help you generate pediatric CT protocols tailored to your institution's guidelines. Follow the steps below to use the chatbot effectively.

### Step-by-Step Instructions

1. **Provide Imaging Study Details**
   - **Type of Imaging Study**: Specify the type of CT scan required (e.g., CT of the chest, CT whole abdomen, CTA Liver, etc.).
   - **Age of the Patient**: Mention the age of the patient.
   - **Body Weight**: Provide the body weight of the patient in kilograms.
   - **First Study**: Indicate if this is the first study for the patient (yes or no). If not provided, it is assumed to be "not first study".
   - **IV Cannular Size (Optional)**: Specify the IV cannula size (e.g., No. 22 or No. 20).

2. **Receive CT Protocol**
   - PedDesignGPT will generate values for the following parameters:
     - **kV**: Kilovolt based on body weight.
     - **mAS**: Milliampere-seconds based on the CT scanner used.
     - **Noise Index**: Noise index based on the type of imaging study.
     - **Delay Time**: Time interval between IV contrast administration and the CT scan.
     - **Contrast**: Amount of IV contrast in mL based on body weight and type of imaging study.
     - **Rate**: Flow rate of the IV contrast calculated based on the provided formula.
   - These values will be explained with reasoning.

3. **Formatted Protocol**
   - The generated values will be used to fill in the following template:
     ```yaml
     `protocol_name`
     BW: `bw` kg
     kV: `kv`
     mAS: `mAS`
     Noise_index: `noise_index` (`is_first_study`)
     Delay_time: `delay_time`
     Contrast: `contrast` mL (`contrast_per_kilogram` ml/kg * `bw` kg)
     Rate: `rate` mL/sec (`rate_calc`)
     ```

### Example

#### User Input

```
CT of the chest, 5 years, BW 18 kg, First study, IV No. 22
```

#### Output

```yaml
chest venous only
BW: 18 kg
kV: 80 kV
mAS: Auto
Noise_index: 20 (First study)
Delay_time: 45
Contrast: 18 mL (1 ml/kg * 18 kg)
Rate: 1.1 mL/sec (Rate: (18 + 15)/30)
```

### Key Guidelines

- **Protocol Name**: Automatically generated based on the type of imaging study.
- **kV**: Determined by the body weight of the patient.
- **mAS**: Depends on the CT scanner used.
- **Noise Index**: Varies with the type of imaging study and whether it is the first study.
- **Delay Time**: Specific to the type of imaging study.
- **Contrast**: Calculated using the patient's body weight and study type.
- **Rate**: Calculated using a formula specific to the study type and must be within the limits of the IV cannula size.

### Tips

- Ensure all required information is provided for accurate protocol generation.
- If optional information (like IV cannula size) is not provided, default values and assumptions will be used.

By following these steps and guidelines, you can effectively use PedDesignGPT to generate accurate and institution-specific pediatric CT protocols.