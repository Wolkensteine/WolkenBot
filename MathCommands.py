import discord
import datetime


async def Math_command(message):
    if message.content.lower().replace("!math.", "").startswith("root"):
        inputs = message.content.lower().replace("!math.square ", "").split(" ")
        temp_text = "The " + inputs[1] + ". root of " + inputs[2] + " is: " + \
                    str(float(inputs[2]) ** 1 / float(inputs[1]))
        embed = discord.Embed(
            title="Math.Root",
            description=temp_text,
            colour=0xcc33ff,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)
    elif message.content.lower().replace("!math.", "").startswith("square"):
        inputs = message.content.lower().replace("!math.square ", "").split("^")
        temp_text = inputs[0] + "^" + inputs[1] + " = " + str(float(inputs[0]) ** float(inputs[1]))
        embed = discord.Embed(
            title="Math.Square",
            description=temp_text,
            color=0xcc33ff,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)
    elif message.content.lower().replace("!math.", "").startswith("solve"):
        inputs = message.content.lower().replace("!math.solve ", "")
        await math_solve(message=message, inputs=inputs)
    elif message.content.lower() == "!math.help":
        embed = discord.Embed(
            title="Math.Help",
            description="Use '.' instead of ',' in case you are not used to the english version\n!math.root"
                        " n number => nth root of number\n!math.square number^number => number^number = ?",
            colour=0xff8c1a,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Unknown Command",
            description="I can't remember this command :frowning: type !math.help to get some help if "
                        "you need it.",
            colour=0xff0000,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)


# math solver
async def math_solve(message, inputs):
    print("Solving the following input: " + inputs)

    # Mathematical operators
    # (
    # )
    # ln()
    # n.log()
    # n.root()
    # x^n
    # *
    # /
    # +
    # -
    # =

    # Declaration of variables
    symbol_array = ["ln", ".log", ".root", "^", "*", "/", "+", "-", "=", "(", ")"]

    given_message = message
    given_input = inputs

    extracted_inputs = []
    amount_equation_symbols = 0
    equation = False

    output = discord.Embed()
    output_description = [given_input]

    errors = 0

    print("Extracting inputs ...")

    # extract inputs
    for i in range(len(symbol_array)):
        given_input = given_input.replace(symbol_array[i], "%" + symbol_array[i] + "%")

    print("Added split symbol '%': " + given_input)

    extracted_inputs = given_input.split("%")

    tmp_extracted_inputs = []

    for i in range(len(extracted_inputs)):
        if extracted_inputs[i]:
            if len(tmp_extracted_inputs) == 0:
                tmp_extracted_inputs = [extracted_inputs[i]]
            else:
                tmp_extracted_inputs.append(extracted_inputs[i])

    extracted_inputs = tmp_extracted_inputs

    print("Extracted all inputs:")
    print(extracted_inputs)

    if len(extracted_inputs) == 1:
        errors = 1
        print("There were no arguments found!")
        output = discord.Embed(
            title="Error!",
            description="No mathematical operators were found!",
            colour=0xff0000,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        output.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                          icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                   "WolkensteineIcon.png")

    # checking if there is an equation
    print("Now checking for '=' symbol (to see if it is an equation to solve) ...")

    for i in range(len(extracted_inputs)):
        if extracted_inputs[i] == "=":
            amount_equation_symbols += 1

    if amount_equation_symbols == 0:
        print("No equation found.")
        equation = False
    elif amount_equation_symbols == 1:
        print("Equation found!")
        equation = True
    else:
        print("More then one equation symbol found! Quitting!")
        errors = 1
        output = discord.Embed(
            title="Error!",
            description="More then one '=' detected!",
            colour=0xff0000,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        output.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                          icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                   "WolkensteineIcon.png")

    # If no error occurred try to calculate the result
    if errors == 0:
        print("Solving math ...")

        print("Getting positions of mathematical operators ...")

        # Mathematical operators
        # (
        # )
        # ln()
        # n.log()
        # n.root()
        # x^n
        # *
        # /
        # +
        # -
        # =

        # look for all the operators
        positions_of_brackets_open = []
        positions_of_brackets_close = []
        positions_of_lns = []
        positions_of_logs = []
        positions_of_roots = []
        positions_of_exponents = []
        positions_of_multiplications = []
        positions_of_divisions = []
        positions_of_additions = []
        positions_of_subtractions = []
        positions_of_equal_sign = []

        for i in range(len(extracted_inputs)):
            if extracted_inputs[i] == "(":
                positions_of_brackets_open.append(i)
            elif extracted_inputs[i] == ")":
                positions_of_brackets_close.append(i)
            elif extracted_inputs[i] == "ln":
                positions_of_lns.append(i)
            elif extracted_inputs[i] == ".log":
                positions_of_logs.append(i)
            elif extracted_inputs[i] == ".root":
                positions_of_roots.append(i)
            elif extracted_inputs[i] == "^":
                positions_of_exponents.append(i)
            elif extracted_inputs[i] == "*":
                positions_of_multiplications.append(i)
            elif extracted_inputs[i] == "/":
                positions_of_divisions.append(i)
            elif extracted_inputs[i] == "+":
                positions_of_additions.append(i)
            elif extracted_inputs[i] == "-":
                positions_of_subtractions.append(i)
            elif extracted_inputs[i] == "=":
                positions_of_equal_sign.append(i)

        print("All mathematical operators categorized.")

        if equation:
            # Beginning to solve equation
            print("Beginning to analyze equation ...")
        else:
            # Calculate the result
            print("Beginning to calculate the result of the inputs ...")

            if positions_of_brackets_open or positions_of_brackets_close:
                if positions_of_brackets_open and positions_of_brackets_close:
                    print()
                else:
                    errors = 1
                    print("There was a standalone bracket!")
                    output = discord.Embed(
                        title="Error!",
                        description="Standalone bracket detected!",
                        colour=0xff0000,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    output.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                      icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                               "WolkensteineIcon.png")

        if errors == 0:
            print("Solved the math. Now formatting output ...")

            tmp_output_formatted = ""

            for i in range(len(output_description)):
                tmp_output_formatted += output_description[i] + "\n"

            output = discord.Embed(
                title=given_input,
                description=tmp_output_formatted,
                colour=0xcc33ff,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            output.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                              icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                       "WolkensteineIcon.png")

            print("Output formatted. Now sending output ...")

    await message.channel.send(embed=output)

    print("Solver done.")
