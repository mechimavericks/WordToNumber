.. cat > source/usage.rst << 'EOF'
Usage
=====

Basic Usage
==========

.. code-block:: python

    from WordToNumber import word_to_num
    
    # Convert words to numbers
    result = word_to_num("one hundred twenty three")
    print(result)  # Outputs: 123
    
    # Handle decimal numbers
    result = word_to_num("one point five")
    print(result)  # Outputs: 1.5

Advanced Examples
===============

.. code-block:: python

    # More complex examples
    print(word_to_num("two thousand and nineteen"))  # 2019
    print(word_to_num("two million three hundred thousand forty five"))  # 2300045

.. EOF