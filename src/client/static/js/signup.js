import { Helper } from "./JSModules/helper.js"
import { APPEAR_DIRECTION, ToolTip } from "./tooltip.js"

const g_Helper = new Helper()
const g_ToolTipManager = new ToolTip()

g_Helper.hookEvent(window, "load", false, () =>
{
	const form = document.querySelector("form")
	if (!g_Helper.isValidElement(form))
		return alert("Can't find sign up form!")

	g_Helper.hookElementEvent(form, "submit", true, (event) =>
	{
		const password = document.querySelector("input[name=password]")
		const password_verify = document.querySelector("input[name=password_verify]")

		if (g_Helper.isValidElement(password) && g_Helper.isValidElement(password_verify))
		{
			if (password.value != password_verify.value)
			{
				g_ToolTipManager.hide(password_verify)
				g_ToolTipManager.setText("Passwords don't match")
				g_ToolTipManager.appear(password_verify, APPEAR_DIRECTION.RIGHT)

				return event.preventDefault()
			}
		}
		else
		{
			alert("Can't find password entries!")
			return event.preventDefault()
		}
	})
})
