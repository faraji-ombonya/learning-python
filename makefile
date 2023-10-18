pr:
	gh pr create --web -B master

push:
	git push origin staging

ppr:
	git push origin staging && gh pr create --web -B master