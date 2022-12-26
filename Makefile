all: install build format test
install: install-client install-server
install-client:
	pnpm install
install-server:
	pip install -e .
build: build-client build-server
build-client:
	pnpm run build
build-server:
	rm -rf build/ dist/ policyengine.egg-info; python setup.py sdist bdist_wheel
publish: publish-client publish-server
publish-server: policyengine
	twine upload policyengine/dist/* --skip-existing
publish-client:
	pnpm publish
debug-server:
	POLICYENGINE_DEBUG=1 FLASK_APP=policyengine.server:app FLASK_DEBUG=1 flask run
debug-client:
	pnpm start
