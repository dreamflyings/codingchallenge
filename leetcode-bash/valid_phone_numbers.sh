#!/bin/bash -e

# ### Problem ###
# https://leetcode.com/problems/valid-phone-numbers/description/

cat valid_phone_numbers.in | perl -nle "print \$_ if /(^\(\d{3}\)\s\d{3}-\d{4}$)|(^\d{3}-\d{3}-\d{4}$)/" > valid_phone_numbers.act
diff valid_phone_numbers.exp valid_phone_numbers.act

