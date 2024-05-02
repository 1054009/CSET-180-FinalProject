from app import app
from database_session import database_session
from datetime import datetime
from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from scripts.object_util import to_json, objects_as_json
from scripts.user_util import create_user, register_customer, get_user_by_username
from template_renderer import render_template

@app.route("/test/")
def test():
	# test_user = User(
	# 	username = "jdog123",
	# 	first_name = "James",
	# 	last_name = "Douglas",
	# 	email_address = "jd123@gmail.com",
	# 	password = "awesomesecure456".encode("utf-8")
	# )

	test_user = create_user(
		username = "jdog123",
		first_name = "James",
		last_name = "Douglas",
		email_address = "jd123@gmail.com",
		hashed_password = "awesomesecure456"
	)

	# print(to_json(test_user))

	test_customer = register_customer(test_user)

	print(test_user.as_customer())
	print(test_user.as_customer().as_user())
	print(test_user.as_vendor())
	print(test_user.as_admin())

	print(test_customer.id)

	vendor_user = User(
		username = "mrdude",
		first_name = "Brandon",
		last_name = "Smith",
		email_address = "afagafsf@gmail.com",
		password = "hisafe".encode("utf-8")
	)

	database_session.add_all([ vendor_user ])
	database_session.flush()

	vendor_vendor = Vendor(
		user_id = vendor_user.id
	)

	database_session.add(vendor_vendor)
	database_session.flush()

	spoon = Product(
		name = "Big Spoon",
		description = "It is a comically large spoon",
		vendor_id = vendor_vendor.id,
		inventory = 5,
		price = 3.25
	)

	carrot = Product(
		name = "Carrot",
		description = "crumhch",
		vendor_id = vendor_vendor.id,
		inventory = 3,
		price = 5
	)

	sock = Product(
		name = "Socks",
		description = "yay",
		vendor_id = vendor_vendor.id,
		inventory = 3,
		price = 5
	)

	database_session.add_all([spoon, carrot, sock])
	database_session.flush()

	hahaball = ProductImage(
		product_id = spoon.id,
		image_data = "data:image/png;base64,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".encode("utf-8")
	)

	database_session.add(hahaball)


	hahaball = ProductImage(
		product_id = carrot.id,
		image_data = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAACUJSURBVHhezXsHWFRX+v47vcHA0IYmTUBA6YiigIq9956oKZuyiWmbzW+T3U1Zs6mb7KaY5pqsuzGamMS4GgvGghUbiNgAFZA2wMAMTGfK+X9nAGMSY+Ju9nn+7/N8c8+999xTvvPVc+8I8L+HlCjqOorvIxWRkkhIZCGyEtUSVRE1El0lqieyEf3P8L9iQAhRJtFoojyiaKIgIh+iXgho3szTW5ZQ2dlX7gVnhp6IM+I40T6ik0TNRL8ofkkG8LZS6WcBA6ZQeQiRhN+YWhCDAWKGeF8PogaqIZO6sX3PJYy8Iw92J0PFrtOYMS8axm4nrra6cKnBgvq6buw8fG3xOXcuCgQoZgwbqXyKyMVv/Lf4pRgwjNbwHhrlDCrzlcZd2ckYF6zG1RYdRk0fhOxJgyAKl6Fx/zEUl1QhfaQGOXOGwi2T4tCmA7hy3ogpxARtejp63GLs2rAPZ6oNCI6Q4fhpYNcOExpbu3nTXcSIncSINVTmkvEd0blV/LcMGEj0MNFSogB+4dWcAkwIVSMu0hc+czPRKbbgq6ffw7SnZ0KvkuKbtf/GzMcnIVpjBAwNgIIe8g/CuctK7PhgL2bdVwCBRI6vP9uLZfdnQaYSwGAxoaHFhU2ba/DaKq4ZXnC78SXRX4jO8Av/CUR9x1uFRATBChL196k8mUgxjH42zfk1Ft6xAlqlC1JzO1AwCAoydeLmdvz9XztxfutRTJyUCN/4IHQ2tcPY0gmj0YEuiwjKAF/ImQXrXj6IU0cuYNbt4YhKiodQpoDRdQXyABsGD/NB8gg/7D3vgtjjlrqtnnTqdqaABgPmZYKT6JZwyxIghDCaevuzG2xxqFgrnCgNBGMmPBKTgiHDsmAeEoHWygNo0V1Bm68QJms36vV6nDiuR2AgEJiggKWZdFtGbUmJ/0wAt5PUmXyFIliOqyfssNLaZtzmi8ikQPhppRAHmOEXJoZvmADJ2iE4fcqFP6yvgMZXhFOf6GBscoOY8DVz4/9oiOd6R/rzcKsMGEr0DlHONGkilodOQoXpDGSCZiSTGJ+2NOJy61W4yNaHDYxAqNCJ/eVtGDczDmPvHIlzF1tgKTuEyY9Og9BfCUFrJTXVA09wEhx24LNXtiF+ZAJNPBRf/LMCx3e2I2OOCm2tEjR1OOEkaRqVG4nEDDU+LW2GNFKFsCQVDr3XiOovSeKAGprRSpKGXfzk5+BWVGAi0cdEyYWiSKRKQ2BwdOBr0wm4xHJ4ZEKkBqkxKX0QFr/2ECZNGoru8gsIRifuWVaImEXDkUge4PSWEgQPiUZisgJqVQ/UgTL4BUhxtrwDru42LLw3HTGp0UhINONynR65E/3x2OMZmDI1FAGDzGhh3ThVboKezEfpMStU/jKIAtSQR6tgrDCSjGEqURPRz7ILP4sBAgim0WEdURg/HywMRaWzCRccF/CKtgB3TX8I44bmIY1cd4RWDZ9QXxw4X4MTJ8tw31OL4KcS05BaILF3IiIrFhveLkWM1gr/jDQKh9Q4V1yOXf+sxLJHMqAS2eG2tkGitCA6VYZ1b7ciKl6FmHQRxJFWhGeKcFtBKhaMiwejNja+1YJWkxD+ZEMMejP5CKeCxHoiDVpHQy3n470ZfpIBQggmMLB/UDFkjHQCHlcNh8ttxAifSNwRNAxVPc3ICQqCUkwuKpJkX2jDsf1HsOn97Xj0xaUIXkaxUCAp+EES93Af+I7KgCZciq/eP4j0vHB0kWv718snsPT3+QjPyqFuPGDdDXBLFYhOTCSS4k9PnIE6xYGQcCVihOEwyuxostqw54Ae99+XCpndTfZGgMJJBXDbfNBR28ijz3ECkaieDBTXsx/FTRlAk8+l4fyLiuF/US7Fn8IfpfjVhjLTbjyc8SLSwtNhMZdh96ktSBqWDtmkfNTUV+OfO7/GygWFiIoMhMtPCldtM5xtejhcdnQ7zDRgPS6dNeLsqXqc3FuH0Bh/JKUGwGyVo8dogMtuIiMpIyMZAHUoSUqUAx+vJqYPC0JKQAiOtrbimdXnkTYmELeNGAJ3pBgfH6jEE0seRNKCXLjiwqHffkXawyxjKOKsIEt7qXdGP8SPGkHyLJFk6b+iYvafZYvxuGYSjGjDY+0f4fHAbGQkLkaruAP1Tf/CWzX7EZI2GIXD07DlSAnS5S4MHRiGRrMZeosBen0rrL5q2K1mmCvccKnJNcZLoW9yQiQTwD9YjJ66Hq8nkJEWy8IUkPgJoAgUwidMCDV5gMPFVijCxRi9QIPNmzogC1Bh7F0RMGolsEkUOLnfiNYdAch5eiRyFctx7N1ivPfgg3wqtZAp58BhpXDqh/gxBoiEEL3ngftufrIv4jMU+mbg9bqHEC2XIc83AlutZ/FFdyX2wIABiRlosJAZr7vofbgf0ygmnJA3EKqUUKi7jVAp3ZDFB0KpYWg414C928iSURw3964Y+MdGweImJumvwtJtQKfZAbtQAV1bDz57UwcrMaapg7dK0UcfuAkRjAUSpsYjLSsR5Zva0ekbjfsXv4xvth3G+udfh/XYaTCh4Bt6bI7XX38PN1QB8vWLPfA8O1U8XvSc6j4YRTY4iFXHu/+NRFkQnuzYg7csZ1HroUnTBAqnzMUfnlmFRfc9gvxJs0hXw1Fx7DB6KKVZPCsDc347Hamk9wn+LsTOzELEoGCc2n0ak1ZkICE3AuYOPcYsHoqYIUMQT2lTcpQdGSPUiBwShcoaC77Y1wmTjSeNDKPGTsYfX/4bJsxeRNKSiebdQnxDNiTELoY2MxhnDuuRFZeHC5cvYPCypfDYGdoqKuNoSTuJAUd6Z3hzRBKdJWK7w4uZIa6ePS2ZxO4T5bDZ4ngWJVDwJaDwxbsUXlqzZg1r7exmBidjpzoYO9hkZx8Vl7K8iTO89997dhyzb5zB2KdFjJXNZAc/GsH++X9a5rbfz+zmB9lbv9ayiq/zGLPdzVjNZMYu5rLzBwaz2XNCrvXBacmSJayqqopx9BCdpQ63X2hjL374GRMhmsEXLGh8GAt5fBjLevF29kxPA5t1oqT/+SYIBKl0vDnI5b1IB5r0XaxLW8ZOBm9kc4WpTAbJtYFcP/mXXnqJuVwu76A4Gro9bG+Dhx1tZ2xr5VU2584HvPXWrxrJWMUSVr8mkz03QczaS7IY61zEmHkZq9+XyZ6dJmPtB7IZuzSWXS0tYBML5L198SC3r6+tW7f19dKLFitjJc2MlVJf60vKWGpOfm/dKD82YMEYdv+n69niy+fZoL+91t8Gd+VclK7h+yrAU9jX4wThPisk01BiLcYW6wZUwYROUh/nDRKvhQsXIieHu69eCGnEburKQ9Gt3NcPyZk56Oww4JUvtmBcHMXxu+pQtCAWCYPIEnaTUls64Bcoh1MixZFvWjFoZCLe2WzA2nX11BaNmg+7D8OHD0NWVhZEIhG6urpQVa+DivpwUAag0YZhSHY2KkoPw3D5KlQjwiFPCkDnoSq0d5jQdfAgbyKepOAoHfnGixffYQCtPo+lxytown7kb4sC5yBQIMP2nm1o79+8+B5MJhOSk5OhUChQXl4OHt7Hh/ojmMIRNcU/vr4qMpJJ2Pjpfny04SRumxyI8XfnQ+jnTwygzI7PUptE4W8UTpVU49/FrXhhTY13g+S6uXuxc+dOKJVKtLW14YMPPoDYbcfkgmxoyJOIiFOqwFBKoJKxfcM6mMsasPzRpygMX4A2jS80Eh80nTjG4wOef24m+n7z3m2qBuIQ+9BnNesKOc3a466yO+SzmF9v5R+QUCi8Vh46dKj3WFtb2yeg38LiZuztjzZ475e8OYQx4zLmNixm7qo85q7NJ1twL2PWO9mFHdnX2hPQOPrLNzrntH79+r4eemEmw3Ce7MJ9f3zZez//4eXsEfMZ9iJzsNdr6xmSU/n1LiK+S/UD/IaILZTMZ4bwFsaCy9kXPn9kMwXxTB0SxnwiE7yN3mxgK1euZBaLpW8430WzrpXlFoxld40F++TJSPbhkxFs7e8HsLV/HMA+ei6WbVgVxV5/NJIpffzZjCV3faePH6MTJ070tf5dHDp9ge73jmt4yTtsGetky/RGFjh+Zu+zAuFf6ehFv0EghfTu5qDH3QZnjx4dlMld6DmNUKbG0FFj8eqL3DbS0yRqNGlv+ftYsWKFV0RvhDBtCO66bSHW7qElEKoolRVDoxJAoxTAVy6AUxqELbsakZE7Ak8+8gDmzpnd9+S3uL7fV199FWlpFAjcANlJcXj8d095y/q9JxFi7YHQSKF6RBzEMYk0CQ9P7ML5/X4GcPeQM1s4EWmCFHSKLJRKdSJNGkGBrxUZSQlYPn86Pt3It+N6mdAPXk6kmH3fvn1eA3UzDBky2Hscu2wYZq0cjdlzIzF7XgTmPliIGfeMh4JSrXFjCpGbk4mnn36GMspJ3vr96O/3lVdewb333guplKv0DyGXSTGM2uB7zia3HuFX2hDZWIegonwMmDmTVyEuYDgvkJnygp8oZ6kWY6AoGiXGz9FNVj9S7KHE+iJWUZSmoEbnzZ+PM8kpOHz0CKqrqrzWeAgFL/n5+Rg4kO+O3Rzh4RH0m4jmFhsS4kJpRrSiPW5aWhlsZMp3knTcdmeU1y6mpafjww8/xJEjR7zGlRvb6Oho8gTDkU3WXka5ws2QwMdDy+srFePz/TvBXFJEFRTBpJSg9o1XufHPJ+Jbat5wmBfY576fsC0+G1kclQsEyWyWqNCrM19++QUx/1t4PB6vrlut5IhvAQaDgRWMnsq+eieFsdqJFMlQ8HOOqH48u3CgyNvXjh07+mp/C5vNxsxm83fijZ9Cc3Mzi4+NY8gbxERj8phvXhEr3LWfFe473GsHAB4VKrkKBBNxkcBL5ifwifU9r148HfYCno/9G7/Mla/32Aeui1zXueu7FfD6EZFaGBvPA1bSSSmtIl9Juw0Vhy5769zIhsjlcqhUKq/E/VzwunJa/SeffAF33Hc3TGQHqj/8BKXPvwGBD58yYoki+Vx56BuUJ8jCavlaPCD7lfeVjcF+CcFOo9c3OhwO+u0FMReOnh7Q6sNE2Z6RApIOg4GCjQ606fVoa9ejvb0NOp2ORL3FSzpKX1vJd3P/LSDP+c3X1L6Juo4l0xOdgiadE5vX8JdAFEB5PKDV9gY6Xd3d6O42kfibQRIHkgTvWNxuUpufAGeAkjJQf20wPGYbRUpqZD50L+asegIhI71e0JdoILcBnAGBBZLRSFOPxJquv+K5wI9x0LwN2QI7RoNswslSyBVKGM0mGGmynZ2dNDgTemigxAkvM1w0OInTgR6XE9VmKyUnNmilHorwRBBSBukmr2R1edBjuAoNPXboqBHTh0rhobns3GvEmClBsB/R48UXX0dYaIDXDvCdTkZ2QiCSkARIKZtUkOFTUnClJvKFr48CMmpbTHm0lOqo/X3hH+APlVoJG43JQ17m67pN6GySYsT9iyC9chnjb5sP44Qi7Nz1b77OsbwbnvKueU/xNsYox+Afprfx+4gX8JnxEyhcZYgKGIst9btwmMLoBzASWoyHn1iPi64dWIXLWBudgUGzR4LNygbOV+DT1aux55wLr6wsgDbEB26RC0xJ5NNL4ggVra4J775+HI+9M5tW14N1z2zFY88XkdTJYWnRQQ43RFIn3EoLXIH+qK5rxAOz2jCF0vvpi2gxaRRdzlb8vZhCOvLOeURWHwoejaRNXSFgB/wQGqKBMcqJWpEDD0x+AWl5o/DaM69g5JO/QdXBEuxdMJemjVVcqRYQ5d8mnI5Gx2VECZVIF4bC39OKNaYvsXjASgiUHuSTV5gbMQyxoUKEh7iQFD0QLqEbJ5srMTo/D4GUutZerMLzG0/hiXsKkPvINMhSI6FoaCcPQjaDzIUyIRjy3HT4R/nBaejApfI61JyowYhpmYgflw/NgHiEBCkQIOiBxl+KgIGxCBqYRm42HGqtFbs3dGL6HZHIzRoIpzAImze14I6HEvDig2MQOzwC4gJ/jBsVS86lG7YCBaJHD0TlYSNyly+EMDAW5Veb0Wqxw03S3PQxz4uIP/SznChtinAMytkZzFcvgprZ4adOhEEowYG2NWjsOoYZMXfDV50CmMvJKvlAlDEbgyio2H3lKzSQzse0tGH15mJkh/pg8ZJCiIrI58tIz6tIt1kPlSmX8JOABWsgcNkQ6mPCrq2tZAdFmDw3DkJVBOm/FMzSBWbsIDPNSISpvkJNKtAD/3ADyk+14nKtE/JYK1b/pR49ZMvuuX8wkhShaIQdnaRm88Tp8NNo8Nn+KzBWN2PeqAegyUrHBVKUeKkfqosPwCc+EQ3r+Js1NHEbQLZZgUPuUmTKhiNCRQGE4wrprRZTZDNwZ/VbmKccSGJHiRvJmJ0Gb+8RwtHdQgMzYEJYGl6rOY1LHc04b7JhydBEHD90AS6HBYxEnVXWwOW1BS44S11w7bwIl4cbVSdMdkaSAHzx0Vmq00zhgA9NXk/8olRSRMmQzAmBphoeGT0n60JwuBLHt9rRUmdA3Tk3xvzRD6cadahpdKBMaoGDosu9vlfQrnVDI7WjtUaNnJWj4EIIBXQihKYkokT4NRyXr0ARHw/bpUsUgwKfCyGaqyK9+0D2DgbLU9HuKodOpIdFSGJn2g4FWe4A9MDJ2mEVqWFiBlh6qEN6WKiQwEz3u9wu+NKKO9weNJOR446W22r+nvtbH/JdRJMHdJNwNPLKBEq6vKkaD3F4jMcHx9vgeaiEzvyihCQp1J6TQRoghFssQBdzQ6fyIEwphshPCoPGAz9ff7gahcTQEETmjIA7PAki30FkV4KgO1IO/a596KwsgaulcQ/vYz3RkjiEkvjMgVwoh5D0XyVRk+4GotJyAFfJGM7zHYHPreexw8Vf2f8c8Ka/Bfe3/Eo/cfRHJHyC/PVe7/vu/qt96H+AKytvhG7xTwsUlENIKeUWEbeEcrrA74uE8JDXkIXLYNBbETMnF7HRhSRVIaizkBwIlGR07Tj/7jrY27y75Tt4068TPcp9wg6/PShQj4GnpwZCXw265WK8X7cSGjIqURQKf2w6i385qjCYQlcFjYavioJ65vpqIZHmRz5GPhni/7VJ9+P6cj/6p8ufkQnEpKm97ZHPAMV9JHeMpKCXPFSRH/k93hvfoOmPCAxUMtJ50q8DYNb1IC4rCXqNFPfctRqRsgx8Q3YoRyDFoR178Y/X/g7B/g0g4VnP+UaRL6ZOp0TIRsYvVz4UUg/JMMw4bDkMFxm8GdEP4pO2LdhjO04dCTCa1CBCIEcQNehDy8GH0bvTICQXJiQRFniZI/4e8Ul+n769x+GBlNrzE0i8pCaGaOgYSMT7ChZKoSXDHErHcKGMwjg5eS05YogoYIBukAfDnghHAMUCK5c9jI4yE/QUWUrDolFLbTg6zCjbsBWKQXHo3LODd7iNL1IbEYsVxsDt6sZp4246E8BirUJx66sYJo1EkEiBkYoYVNEK+HvXVuAVW74SncQ0K3N5z6+n/pW9FeLPmWml2j2Ug1KbXk/wA+qty8Elql/KvFJiY6je0AL1EDUuBzSC5Uqxa3cxGpwdFDlIUXygFJ2xAyD1uxbCt/HnuVJ3WDx2jBONwTbXAfQoI3CeecgeSBBnp9u6T5BF9iBFpCVr6vZ2yIkP1kFyxFnyS4G3xSdjIMbaiAk/1XI/4+z89yrRABHUmT7k9mqhTc2EqtmK6AaGWKMJlp17MbUoD6oO/u6UpgJBLUWcAv4SseskO4VgUSQCPH44ZNqBQ9bjmBDyKGR+Y6meDFL/QvjIYvlTXnD9szJyU7/g5PvBW+QTMzKHl8E364Pf4Qzr5iaUnPqjcyYiQR6MIMp1Zvoux7QJi/DZ3mJsIUnIHDEUMb4+6KrwvjjmvqqWtEnWQie1J9lZrOlZhzbWgqc678Bxxz7yAhHoEvmihxjrttXBhybMwUXRRmXO+X7wgXBxuhnxOj8+le+C1+tnAlewmz3XQ/p/ldiQukKDqKhACuF9oLd1oLzzFAwqJ0q/+ApHXn8fFy434B9/fRfVm7/gj3HJr+tv92mi5x4W3Y2x4tHY5NyAi8SQOGEYmMdIkiGGmmTlc2clamhUU4V8m9RF/t3jNV6cET2kMtwTcEvcSeecVdwwcp/OPYyKWCCn2jJKcPqNXv8kOf0YuB1Qeo0ib+mH4CqjI1Xc5elC7HwfaEf7w9Imhb7dgpb2VopfCiG4aIJ6RBGSZ01D46nTOPOHR/mj/POe+/nCcPBNc4eZeJ0rH4FwgZYG2ID7VHPwVPgLmOQ3GYnyOOTJezdT26lDLgUcHcSI3cyGEmKHW61BbkQCFkUk4c7gRCxVx2KGNAI5ZDqV9EQpsaWEdHsP1S8mauR67mVfr4TcCFz8uS3o8arCD8FHofdQNEXw0UgQ4tTAP1aBGdPvwd9WHcew5fPIwDngEzUAo0flIcxBGVMvDhHxPSkv+JcV2xMEA3MfkdyFBtaIXMVQXHKfxSPRv4fERnUl3TglpdDy3AzwF1ZJ5AYv0QT4l4t/GjwS48NjEUqpqoYMpyzAD0J/khIfmrZYTNGhG92Uz5s6OmDo1ONSazPKGutxqOUCyrzdA9kkF/600jw2v161OLgUyL0ukdzddeCD53HCfrcROlKBJ4sLsXT8dOxCC10tRIQpB2+8+hrUGfm4tP8khs6agdKnH0f94cP8xcg4oiu97rf3c9SoThhGbXfvwe2K27HAfwkOm3bDYjuDBJ6cU/irJDGr6D6HCk83yYcL3XR5+6h5WDYwHdFyJfzDwiAfnQdxZhpEcdEQhWkhDg6EPCAAfkEhCI6IQFRcPNIHpaAoORXT49IwXh2CQI8AX3W3kt12kcgKaLLf9Su9breXCTx26AevpSdprKCFQAwQGeOLiKwBqBFbaXEs2PzpFuQG5CFn1mycqDiHQ3//BF2Hd/MW+IsRbzp4veRxy+B9AR2HKEhtFiyVjcKXXetRz6iaehpa7MQidwOv4l2l570rHweJiyywhlZ80mggLBS03ORhqak2sgb6rt7z/l0lKYVI/mrIYmIwIC8Pk6fOxItTFuJE0RI8FpeJE6Qm50g9eFh8PRM4A+ykBteDX6sj9y2ivGDuawNRUV+LT9tOEBOTIKRkqay0DvapOQiRSzE9LZmEnn/uQM0IBL3b24TrGcB9w795oRpN5H7siFLkYGnI3/Cx9Ryc5A3OeyS4TZWO5xSDeDUefPUqoYsGlhhLoSCJKGVnsNFk+XW+l8ilh1P/viJ/iBIm8G0tfi0wEMrMdOTk5WNVThG25c2CWqXBXmKCgxr51gUKSNy5w+sFl4RO8kRVdDVnmQax4wIhibRDXa1FijUbrRta8cQ9v4U8MAJVLS1oOH3t+4gSGgPXfy/6VcAL6oxLwLztrmJZoEtGkxYjQZmAGtNRtJn24VT3MYz3T0N+2FQcNjfj45aTmBAaS4zyJfkLJynwp4iC3Kvwx0xaH/jEOXFmcOKbnWQzJIEBSCQ7MsonGJfMBuy1dCCyz2v0T1xBatAbLAGVFLJ3kBxM+0s00hKiITUFouycEVW6c+gOCkN++nhc+uYEVn+4ARdeXUVPceck4G9Mrn1B9h0GEBqICbSUnuwkYQoGkWIdMW8isa/DOus2yuO7sSB4BiIi5iJD6MQa/T7s1dUhP2QAwiVK0sMBvSvLVaJ/xW+Gfkb0g28bRYRBS4HHULkfTnfqcMRmRAwZR16LM0FO7OD5QgNJ6Cmi3N+rsGDJEMwT5VGW6I/X1uxA1Zl2iAOUOHr0HCKik+Bvs+PqnmLeA08A/kzUm3gSvs8ADr4/PeMYa/F7QLYIk5RFiFCmwOmyo8JdTakyZX62emhdOuRJffFhVzUOtl1FtsgHA8gQggyfVyW8+nGL8JBqyMnfB2sQpOvAQMpIP6o96/3GXs03SOnoQ8ww0aoXe0yIGC7G5KcGUNYoQXO1E7tOXkH5yWYUpUzGqMI5CJw3E4kSDY4++zQ6dDryf4KV1ETv/nsfbsSAdhFdpuByYovzLMYr5yNGnQOd4wJec3yNySJaZUkg9jracNVaDZOnE+cddqytP4tMC6PVopSWryQZO68q3AojuDRwCQrSUP7RCq1bAEOPHdsMzYiidqUk/B5q8zhNnjMhOF6CTsrvt35Tj6N6Pc6UtcJ2xoD5Kx9B4bj5qLTbsG3Vq7i8bRsEItGbFNWt7evpGm7EAIreZBcp7xpWhZZYX7IFWQjGbutOFEkGotWpw9LEP2JC2AQke1rIjUUhNyqfBiTCSzX7IdTpEWV1QkPzFvB3d5wRP/VCw8sj+uEJP5cAP7Ipl+ogstmI8VZsbb6MMG/aDZymTJH7/GW/DUHsYhUmD0/B0zMmQxQlQ0d1CCZMno8Kkw72tHiUffgFLqx6iZ4SHIdIuJIkjH9h/h3ccGQuuOy0dqdoOOP3u48GhrikqHFVYXnIg5ApU/GFfh3yyLJrPR0ID4hDVtpCFJKfr63ajjVdOrxVfQoRFif8uyzwtff0diKiFjkjOPXrvpfouoSu8YlraOJaislo9VFxnn+AgANtDdhFdkZCVc9RRNhNbPjnR1m494FkdAy2Izk0GmqbBu+8fAQpswsQlhiH2tJOBFCQsm3F/bznNpLEu0myLvCT7+OGDOCgyVOuLOCh/7Rd7uNyHatHoTiD9D4AV7oO4ZRhD9ICsiDV5pPlP48rDQcQk5iMx2feA5HbjGdOH8Cmqgo4DAaIOwyQGrqgMJshJIMEJxlj/oU4Vw/+SQl3n1KKAR0U0laTih4jl0X2oIo8wUuVh9Bgt1COQTJJjiaD4rdJS8IRGqmmKyp809GCN94sQ3zWUAzLH4fjpy+i+I2tOPXOB3waPQKR8GFqy+vebwTi681BFZbTMN+lomII1JgvGQaNRIZPrYexKGQ87hi0EDAcwrsXPsJtUx5CaMYQWGpLUFJzHE8cO3Ht2/URlKCOi4pGqjYUCX4UGSpVkEkpzZZIKEwgN8ffGtkpNyC91bsdKDd14B9lZTjq4vs15Jvv9sXiB8JJkBTYuOsq/vrIJDSYXFiyugTOcxoUTkqnuMsHZXvOo307/wyI+CMU/I7U6hVvAz+Cn2RAH35NxPcOZb9TLEGuJBgVtlJ85TyGJapBlAMEwqJSYMXEh6EQtVOSuQsoSMMZlQNr3/8zokMjUet24u0yyrz5NnEfcihmGwA/yhDJ+YYI0NRqwQHvN869CIz1wYO3JSOrwILgTCeiA6MgNmnwuzdLoaW0t7LagK9PXkV80SBMzb0d1hoh1vyJ3HwjF2CsInqWiJd/FD+XAbzi3dTS6xTH+q6Wj8eUgMloV2qwse1DHOjeihR5DJJjs5HkK8UAWxNCJxciKDEINbs3o6z5AooWDqX0Iw0nSivx/v3bkHp3KpweB/QtOrTZlNi9XYflS2ORkBINXfkl9HQ04v4/LUFUchAuNR9GRUMLdE1ytDcJsP+iAZWNVqyYMgxT5xThjMaI6j0WnHzoMC53nHPSyj9LK+/93K939D+OH7UBN0AZhZ/kHex5213n/XqEoSjSTkKiSIJSw3Z0u4wINBvR0dmCbS0VKD5wACeP74aNDFl9ZzfOdpuRkDYA5mY9VO7L+NWjE1E4MhBjc30wemQyfC5XY9K0FKQNjkRdaTWFw2Lo9DZ8+tlZ/H31BZw560A32cnKdhsqWsilh7vwlwd/hSjlQKx/cw82P/YpDLb2DqFI+BjzsDf6xvyT+NkS0A8S1mxy8H9lcBekiSKRIgjC+KBURGoysLVxLeYEhSNp5DR0UFRcc+ZL1HddgY6Y037JDDulCGLKlVRaEdRaJcRSMrMe8jkUyHS1mmA3u+FoJGOTRgFPcBD8Q4TQJkmRWZAKTZg/NpaexI49djx2+xgcP9+Mykob2s+1oXxfDQ+PKzxC9htyEnv6hvqzcCsS0A9SZLZFBKFLx7rSznp0cqlHiezATMSLBNhydQ+EofHIHjAQGWIncjUqDJ2cjcKXF0Lm58BpMmDTf5OF3OHhCJdbEUMpbPrYQZD6q3B6czuWvFKE5c8+gKJRcchPtiIp2x9M5UsT78Rnx+rx8O3ZlB9osWvTRWxbewK6uk6bUCRY42Hs1yTwFX1j/Nm4ZQn4HvIpNfk/Fzz8aybx3ZQ4hUmkKOs6h1S5HAszRiItfSCEI0LhTFHhvXc2IGJoMLrajBiXocSAEQn0lAAX9p9H6UkHJP4a7/8KVjy6gEIEG4yXjmP3xSa8vbsZbeQ1s7J8YG1y46v3et9OiUWCgy4345EOj/F/Ut9vhP9EAq7HVcrJvyLxO0u9B5Y5OyMOONpFPUIZjpIrO9FQC0+UFlrK1Jq/3I+rlDMsvauQ8ggntq0rgXb4ULQ0OVGy9iDm3jsZqXlp+Gb9HkT4qdCpCMb7G8vx4DtnoKe4SNLpwKFNHbh4spsHhMfJtDxHWfUfqMw/7P6P8d9KwPXwocZGEyP4nyhHEXn/X8SRT3GOv0eOvGXpGJ0ZhpCebtQKKaHZUgahqRvTn7gd4XER0FXUYPPOi7hU24HLhm5UXrrOZ8L7X+IjNOJPaK13U5nvvf5/Cc5U/kEgj0M/I+J/V+Gfp/KV42JKJGAxSTxb6D2Pjgugo/jaeR/x/8nWEfEojm/j8o8Q+ZbhL4pfUgJuBD5gvuGaREQK7/0XOT/yf5fzz8H4h0p894RPli8335CpIeJfTHHG8b+gkAJ4d9n/BwD+H950DsYObPEYAAAAAElFTkSuQmCC".encode("utf-8")
	)

	database_session.add(hahaball)
	database_session.flush()

	print(spoon.vendor)

	spoon_warranty = AvailableWarranty(
		product_id = spoon.id,
		coverage_days = 50
	)

	database_session.add(spoon_warranty)
	database_session.flush()

	users_spoon_warranty = ActiveWarranty(
		warranty_id = spoon_warranty.id,
		user_id = test_user.id,
		activation_time = str(datetime.now())
	)

	database_session.add(users_spoon_warranty)
	database_session.flush()

	test_user.warranties.append(users_spoon_warranty)
	database_session.commit()

	print(get_user_by_username(test_user.username))
	# print(objects_as_json(User))
	# print(objects_as_json(User, "id", 1))
	# print(spoon.price)
	# print(objects_as_json(Product))
	# print(objects_as_json(ProductImage))

	return render_template("base.html")
