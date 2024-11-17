"""
THIS IS THE PRIMARY IMPORTS FILE USED FOR main.py
This file contains all the imports that will be used for main.py
All the functions that are from the files in the procedures directory AND the protocols directory, will be placed here

HOW TO USE imports.py SYSTEM:

1. [procedures/{file_name}]: Create functions on independent python files in procedures/

2. [procedures/import.py]: On procedures/import.py import functions/file using the following format:
    (from procedures import (
    '[file_name]' as '[shorter_name]',
    '[file_name]' as '[shorter_name]',
    '[file_name]' as '[shorter_name]',
    {etc. keep going for each file you have})

    for example, for importing particular functions - ON PROCEDURES/import.py YOU WRITE:
    from procedures.other_clinical_procedures import (
        blood_glucose_analysis,
        eye_irrigation,
        splinting,
    )

    or, for example, for importing the entire module (which I plan on doing) - ON PROCEDURES/import.py YOU WRITE:
    from procedures import (
        other_clinical_procedures as ocp,
        cardiac_clinical_procedures as ccp,
        airway_clinical_procedures as acp,
    )

    A. ANY FILE REFERENCING FUNCTIONS FROM procedures/import.py MUST BE REFERRED WITH 'SHORTER NAME'

3. [protocols/{file_name}.py]: Import the procedures/import.py file to utilize procedures/ functions

    for example, for importing PARTICULAR FUNCTIONS - ON PROTOCOLS/MEDICIAL_PROTOCOLS.PY YOU WRITE:
    from procedures.imports import blood_glucose_analysis, ocp

    or, for example, if you want the ENTIRE MODULE imported - ON PROTOCOLS/MEDICIAL_PROTOCOLS YOU WRITE:
    from procedures import imports as proc_imports
    (but this has a problem, calling a function is a lot of words (i.e. - proc_imports.ocp.blood_glucose_analysis())

    or alternatively, for example, if you want the ENTIRE MODULE imported - ON PROCEDURES/import.py YOU WRITE:
    from procedures.imports import ocp
    (to call a fuction from ocp, you would write ex. ocp.blood_glucose_analysis())


    A. To Utilize any and ALL functions On protocols/{file_name}
        you will need to import procedures/import.py using the following format on protocols/{file_name}.py:
        (from 'procedures' import 'imports' as {shorter_name (For referring to any function in procedures/import.py)})

        a. There are ups and downs to using this method instead of 3B:

            I. Benefits:
                i. You have access to ANY AND ALL functions in procedures/import.py
                ii. It's more consistent since everything is prefaced as
                    {shorter_name_for_imports.py}.{shorter_name_for_file_name_in_procedures/}.{function_name}
                    shorter_name_for_imports.py = STAYS THE SAME THE ENTIRE TIME WHEN REFERENCING
                    shorter_name_for_file_name_in_procedures/ = NAME OF FILE THE FUNCTION YOU WANT TO CALL IS FROM
                    function_name = SIMPLY THE NAME OF THE FUNCTION YOU ARE CALLING
                iii. Better for scalability - If I end up adding more functions to procedures/{file_name}.py,
                        it's automatically imported to protocols/{file_name}.py

            II. Disadvantages:
                i. Less Explicit and Less Clear to developer looking at a file in protocols/
                    1. For example, if you are looking at medical_protocols.py, it's not super clear where functions
                        are coming from, you'd likely have to look at procedures/import.py to understand what's going on
                ii. You CANNOT have any functions with the same name in any file located in the protocols directory
                    1. To be honest, I'm not entirely sure if that's true, but with everything consolidated,
                        functions should all have their own independent name, that's the plan to begin with,
                        but if you have very basic functions to do something, it's name needs to be unique.
                iii. Importing entire modules can increase the amount of memory you use, decreasing performance.

        b. I'll likely end up using this system to begin with, but I'll add an alternative option in 3B. Using this
            method allows me to import the entire module rather than independently typing every function I use,
            it's also great for scaleability if I add more functions to a file in procedures/

        c. ALTERNATIVE - DIRECT CALLING METHOD:

            I. Instead of calling as:
            (from 'procedures' import 'imports' as {shorter_name_for_procedure/imports.py})
                i. This forces you to call functions as
                {shorter_name_for_procedure/imports.py}.{shorter_name_for_file_name_in_procedures/}.{function_name}
                for example - proc_imports.ocp.blood_glucose_analysis()

            II. NEW METHOD OF DIRECT ACCESS CALLING:
            (from procedures.imports import {shorter_name_for_file_name_in_procedures/.py})
            For example - from procedures.imports import ocp
                i. This forces you to call functions as
                {shorter_name_for_file_name_in_procedures/.py}.{function_name}
                for example - ocp.blood_glucose_analysis()

    B. To utilize specific functions from procedures/{file_name}.py instead of importing the entire module,
        you need to use this format on your protocols/{file_name}.py:
        (from 'procedures.imports' import {function_name}, {shorter_name_for_protocols/file_name.py}
        ****Keep in mind, you need to use the short name you chose for the FILE, NOT the imports.py ^^^^^^^

        a. Benefits and Disadvantages:

            I. Advantages:
                i. Decrease Memory Footprint - it marginally improves performance, possibly boosts performance
                ii. Easy to call functions - You just write the function name, it's as simple as that
                    1. i.e. if you have a function in "other_clinical_procedures.py" located in procedures/
                        called "blood_glucose_analysis()", instead of prefacing with so many words like 3A, you
                        just type "blood_glucose_analysis()" and the function is called!

            II. Disadvantages:
                i. Read 3-A-a-I
                ii. The biggest issue is scalability, though it's not truly THAT big of a concern, you would just need
                    to always add a new line to protocols/{file_name}.py importing the new function you wrote in
                    procedures/{file_name}.py

4. [protocols/imports.py]: Consolidate all the protocol files and their functions here, this is the PRIMARY
    imports.py file we call on main.py

    A. To import PARTICULAR FUNCTIONS - USE THE FOLLOWING FORMAT:

        from protocols.{file_name} import ({function_1}, {function_2}, {function_3}, etc.)

        for example - if you want PARTICULAR FUNCTIONS in protocols/{file_name} imported -
        ON PROTOCOLS/IMPORT.PY YOU WRITE:

        from protocols.medical import (
            abdominal_pain,
            allergic_reaction,
            diabetic_emergencies,
        )
        (calling this function on main.py is simple, you literally just call the function name, no preface)

    B. To import THE ENTIRE MODULE - USE THE FOLLOWING FORMAT:

        from protocols import {file_name} ****optional: you can use "as" to shorten file_names

        for example, if you want to import the ENTIRE MODULE - ON PROTOCOLS/IMPORT.PY YOU WRITE:
        from protocols import medical_protocols

        (calling this function on main.py is longer:
        if on main.py you import the entire protocols/imports.py as:
        (from protocols import imports as prot_imports)
        you would have to call it in main.py as:
        (prot_imports.medical.bls_adult_alt_mental_status_syncope())

    C. Consider adding an __all__ variable, it's supposed to make imports easy into main.py, though, this is for
        importing particular functions.

        # Export the modules and functions - this supposedly makes for easy imports in main.py
        __all__ = [
            "medical",
            "bls_adult_alt_mental_status_syncope",
            etc.
            ]

5. [main.py]: Finally, import you primary imports.py file for access to everything

    A. Use this format:
        from 'protocols' import 'imports' as prot_imports.

        a. To call a function it's long, but this is what you'd write:
            prot_imports.medical.bls_adult_alt_mental_status_syncope()

    B. Keep in mind, we need to use __all__ in protocols/imports.py so that we can directly call very specific
        functions all the way back to procedures/{file_name}.py
"""