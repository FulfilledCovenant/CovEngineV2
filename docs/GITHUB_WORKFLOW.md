## GitHub Actions

The project is configured with GitHub Actions to automatically build the application when changes are pushed to the repository. The workflow is defined in `.github/workflows/cmake.yml`.

### What the Workflow Does

1. Builds the C++ backend using CMake
2. Builds the Python frontend using PyInstaller
3. Creates artifacts that can be downloaded
4. Automatically creates releases when tags are pushed

## Creating Releases

To create a new release:

1. Create a new tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. The GitHub Actions workflow will automatically:
   - Build the application
   - Create a release named "Release v1.0.0"
   - Attach the built application as a ZIP file to the release

3. You can find the release under the "Releases" section of your GitHub repository

## Local Development with CMake

For local development, you can use CMake presets:

```bash
# Configure the project using the default preset
cmake --preset default

# Build the backend only
cmake --build --preset default

# Build the complete application (backend + frontend)
cmake --build --preset full-app
```

1. **Skip CI**: If you're making a minor change that doesn't need CI (like updating documentation), you can add `[skip ci]` to your commit message.

2. **Debugging Failures**: If a workflow fails, check the logs in the GitHub Actions interface for details.

## Customizing the Workflow

To customize the GitHub Actions workflow:

1. Edit the `.github/workflows/cmake.yml` file
2. Commit and push your changes
3. The updated workflow will be used for all subsequent pushes

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [CMake Documentation](https://cmake.org/documentation/)
- [CMake Presets Documentation](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html) 