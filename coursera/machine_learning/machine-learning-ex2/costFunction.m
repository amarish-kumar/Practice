function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%

% formula for cost function => 
%            (1/m) E [-y(i) log(h_theta(i)) - (1-y(i)) log(1- h_theta(i))]

sum = 0;
% start loop till m
for i = 1:m
  % find h_theta(i)
  h_theta = sigmoid((theta')*(X(i,:)'));
  % find value of expression in square bracket.
  exp = -(y(i,:)*log(h_theta) + (1-y(i,:))*log(1-h_theta));
  % update the sum variable
  sum = sum + exp;
end
% divide the sum by m.
J = sum/m;

% formula for the gradient of the cost => 
%             (1/m) E [ h_theta(i) - y(i)] * x(i,j)


% outer loop for theta values
for j = 1:size(grad)
  sum = 0;
  % inner loop for m samples
  for i = 1:m
    % find h_theta
    h_theta = sigmoid((theta')* (X(i,:)'));
    % evaluate the expression
    exp = (h_theta - y(i,:)) * X(i,j);
    % update the sum 
    sum = sum + exp;
  end
  % divide by m and store
  grad(j) = sum/m;







% =============================================================

end
