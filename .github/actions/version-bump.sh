bump2version $1

echo '::set-output name=previous_version::$BUMPVERSION_CURRENT_VERSION'
echo '::set-output name=current_version::$BUMPVERSION_NEW_VERSION'
