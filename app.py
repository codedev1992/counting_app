import streamlit as st 

input_string = st.text_area("Enter Team Selection :")

if st.button("Compute Team Count"):

    if input_string.endswith(','):
        output_str = input_string[:-1]
    else:
        output_str = input_string

    output_str = output_str.replace(",,", ",")

    ranges = [s.strip() for s in output_str.split(",")]

    numbers = []
    import re
    for r in ranges:
        if '-' in r or 'to' in r:
            start, end = [int(i) for i in re.findall(r'\d+', r)]
            numbers.extend(list(range(start, end + 1)))
        else:
            numbers.append(int(r.strip()))

    # Remove duplicates and sort
    unique_numbers = sorted(list(set(numbers)))

    st.write("Teams Selected :", len(unique_numbers))  
