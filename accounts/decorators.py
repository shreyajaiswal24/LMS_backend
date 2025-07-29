from django.shortcuts import redirect


def admin_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is a superuser,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and a superuser
    def test_func(user):
        return user.is_active and user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


def instructor_examiner_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is an instructor/examiner,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and an instructor/examiner
    def test_func(user):
        return user.is_active and user.is_instructor_examiner or user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


def trainee_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is a trainee,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and a trainee
    def test_func(user):
        return user.is_active and user.is_trainee or user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


def operations_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is operations staff,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and operations staff
    def test_func(user):
        return user.is_active and user.is_operations or user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


# Legacy aliases for backward compatibility
lecturer_required = instructor_examiner_required
student_required = trainee_required
