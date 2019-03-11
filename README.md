![GitHub Logo](https://static1.squarespace.com/static/58ed365f20099e2bf03e0721/t/5a72265171c10bf970879fbf/1521683467932/?format=1500w)

Thank you for your interest in Allevi! We are excited to consider you for our software engineering position and want to get a chance to see who you are as a coder and how you tackle problems. We have developed this Coding Challenge as a way for you to put together a software project with any implementation/framework you prefer.

We have created a data-set of 100 users' printing data. You can find the dataset in `allevi-data.json` at the root level of this repository. The dataset is an array of example prints with the following schema:

```javascript
  {
    "user_info": {
      "serial": { "type": "number", "description": "Serial number of the customer's Allevi printer"},
      "email": { "type": "string", "description": "Customer's email address"}
    },
    "print_info": {
      "files": {
        "input": { "type": "string", "description": "Filename of the input STL file."},
        "output": { "type": "string", "description": "Filename of the post-processed GCODE file."}
      },
      "printer": {
        "modelNumber": { "type": "number", "description": "The printer model number indicates the number of extruders on a printer"},
        },
      "pressure": {
        "extruder0": { "type": "number", "description": "Pressure of the first extruder."},
         ...
        "extruderN": { "type": "number", "description": "Pressure of the N-th extruder."}
      },
      "temperature": {
        "extruder0": { "type": "number", "description": "Temperature of the first extruder."},
         ...
        "extruderN": { "type": "number", "description": "Temperature of the N-th extruder."}
      },
      "material": {
        "extruder0": { "type": "number", "description": "Material in the first extruder."},
         ...
        "extruderN": { "type": "number", "description": "Material in the N-th extruder."}
      },
      "crosslinking": {
        "cl_enabled": { "type": "boolean", "description": "If photocrosslinking was used during this print."},
        "cl_duration": { "type": "number", "description": "Duration of photocrosslinking using during this print in ms."},
        "cl_intensity": { "type": "number", "description": "Percent intensity of light used in photocrosslinking."},
      },
      "resolution": {
        "layerNum": { "type": "number", "description": "Number of layers in this print."},
        "layerHeight": { "type": "number", "description": "Height of each layer in mm."},
      },
      "wellplate": { "type": "number", "description": "Wellplate type used for the print."}
    },
    "print_data": {
      "livePercent": { "type": "number", "description": "Percent of final print determined to be alive through live/dead imaging."},
      "elasticity": { "type": "number", "description": "Measure of final print structural rigidity measured in kPa."},
      "deadPercent": { "type": "number", "description": "Percent of final print determined to be dead through live/dead imaging."},
    }
  }
```

Example:

```javascript
{
    "user_info": {
        "email": "user0@gmail.com",   // Users are indexed by their email
        "serial": 0
    },
    "print_info": {                   // Input data for the print
        "files": {
            "input": "file_0.stl",    // This file provides a 3D view of the object for the user
            "output": "file_0.gcode"  // The file is used by the printer to print the object
        },
        "printer": {
            "modelNumber": 6          // This printer has 6 extruders
        },
        "pressure": {                 // Pressure for each extruder in PSI
            "extruder0": 38.4,
            "extruder1": 89.9,
            "extruder2": 51.45,
            "extruder3": 43.63,
            "extruder4": 70.92,
            "extruder5": 93.25
        },
        "temperature": {              // Temperature for each extruder in Celsius
            "extruder0": 115.19,
            "extruder1": 43.04,
            "extruder2": 4.66,
            "extruder3": 111.17,
            "extruder4": 95.1,
            "extruder5": 104.51
        },
        "material": {                 // Material for each extruder
            "extruder0": "Gelatin Methacrylate",
            "extruder1": "Pluronic",
            "extruder2": "Collagen",
            "extruder3": "FRESH",
            "extruder4": "Hyperelastic Bone",
            "extruder5": "Collagen"
        },
        "crosslinking": {
            "cl_duration": 12415,     // Cross link for 12415 milliseconds
            "cl_enabled": true,
            "cl_intensity": 80 
        },
        "resolution": {
            "layerHeight": 0.2,       // Each layer is 0.2mm thick
            "layerNum": 33            // This print is made up of 33 layers
        },
        "wellplate": 96               // This print was identically replicated into each of the 96 wells in the well-plate
    },
    "print_data": {                   // Output data of the completed print
        "deadPercent": 53.09,
        "elasticity": 47.42,          // The higher the value, the greater the elasticity
        "livePercent": 37.42
    },
}
```

Using this dataset, we would like you to build a web application using any stack you are comfortable with to build a tool for our customers and for our internal team to analyze print information and results. We'll leave the details of the application up to you and what you think would be important for the users of the application. Send us your final code on Github and we'll take a look at what you built!

Some points to consider:

- We will be focusing on:
  - the implementation of the web application
  - the method of data storage
  - the tools/insights made available through the web application
- The overall appearance of the web application has a very small weighting.
- You do not have to host your web application however please provide the execution/running instructions in your README.md.
- Key Terms:
  - [Extruder](https://static1.squarespace.com/static/58ed365f20099e2bf03e0721/t/5a62714a24a69463e4933089/1542379654239/Allevi+2+desktop+3D+bioprinter+extrusion+bioprint?format=300w): Extruder heads contain materials and control the temperature/pressure of their contents. Materials are extruded out of an extruder by means of a pressure pump.
  - [CrossLinking](https://static1.squarespace.com/static/58ed365f20099e2bf03e0721/t/5bc61be353450a6d6aaa454d/1542379654241/IMG_1442.JPG?format=300w): Using visble/UV light to photo-cure the 3D printed object.
  - [WellPlate](https://farm7.staticflickr.com/6118/6252392655_c4285c5aa6_b.jpg): Flat tray with multiple wells such that each well contains a print.

What to submit:

- The GitHub URL to your project

Thanks and if you have any questions email us at info@allevi3d.com! We can't wait to see what you come up with!
