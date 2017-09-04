function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    new_theta = zeros(size(theta));
    % a loop for all the fields of theta
    for j = 1:length(theta)
        % declare sum variable
        sumvar = 0;
        % a loop for all the m values.
        for a = 1:m
            % calculate h_theta(x)
            h_theta = (theta')*X(a,:)';
            % subtract y from h_theta(x)
            diff = h_theta - y(a);
            % multiply with x(i)(j)
            mul = diff * X(a,j);
            % add result to sum variable
            sumvar = sumvar + mul;
        % end loop
        end
        % multiply sum variable with alpha/m
        gradient = (alpha/m)*(sumvar);
        % update current theta in new_theta
        new_theta(j) = theta(j) - gradient;
    % end loop
    end
    theta = new_theta;
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
end

end
