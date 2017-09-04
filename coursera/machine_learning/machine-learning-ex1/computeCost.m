function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

sum = 0;
% for m times
for i = 1:m
  %find h_theta
  h_theta = (theta') * (X(i,:)');
  % h_theta = X*theta;
  %subtract y(i) from h_theta and square
  diff = h_theta - y(i,:);
  square = (diff)^2;
  sum = sum + square;
end
%exit for loop
J = (0.5/m)*sum;
return


% =========================================================================

end
