#!/usr/bin/env ruby
# frozen_string_literal: true

require "yaml"

def load_yaml(path)
  YAML.safe_load(File.read(path), permitted_classes: [], aliases: false)
rescue Psych::Exception => e
  abort("YAML validation failed for #{path}: #{e.message}")
end

def require_string(data, field, path)
  value = data[field]
  abort("#{path}: missing non-empty #{field}") unless value.is_a?(String) && !value.strip.empty?
end

skill_path = ARGV.shift
abort("Usage: validate-yaml.rb SKILL.md ISSUE_FORM...") unless skill_path

skill_text = File.read(skill_path)
match = skill_text.match(/\A---\r?\n(?<frontmatter>.*?)\r?\n---(?:\r?\n|\z)/m)
abort("#{skill_path}: missing YAML frontmatter") unless match
skill = YAML.safe_load(match[:frontmatter], permitted_classes: [], aliases: false)
abort("#{skill_path}: frontmatter must be a mapping") unless skill.is_a?(Hash)
abort("#{skill_path}: name must be oh-my-gh-writing") unless skill["name"] == "oh-my-gh-writing"
require_string(skill, "description", skill_path)

abort("No Issue Form files provided") if ARGV.empty?
ARGV.each do |path|
  form = load_yaml(path)
  abort("#{path}: form must be a mapping") unless form.is_a?(Hash)
  require_string(form, "name", path)
  require_string(form, "description", path)
  body = form["body"]
  abort("#{path}: body must be a non-empty array") unless body.is_a?(Array) && !body.empty?
  body.each_with_index do |item, index|
    abort("#{path}: body item #{index + 1} must be a mapping") unless item.is_a?(Hash)
    require_string(item, "type", "#{path} body item #{index + 1}")
  end
end

puts "skill frontmatter and Issue Forms are valid"
